from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

str_list=["G. Yang, M. Vo, N. Neverova, D. Ramanan, A. Vedaldi, H. Joo, BANMo: Building Animatable 3D Neural Models from Many Casual Videos, in: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), IEEE, New Orleans, LA, USA, 2022: pp. 2853–2863. https://doi.org/10.1109/CVPR52688.2022.00288.",
"R. Shao, H. Zhang, H. Zhang, M. Chen, Y. Cao, T. Yu, Y. Liu, DoubleField: Bridging the Neural Surface and Radiance Fields for High-fidelity Human Reconstruction and Rendering, (2022). http://arxiv.org/abs/2106.03798 (accessed November 20, 2022).",
"F. Zhao, W. Yang, J. Zhang, P. Lin, Y. Zhang, J. Yu, L. Xu, HumanNeRF: Efficiently Generated Human Radiance Field from Sparse Inputs, (2022). http://arxiv.org/abs/2112.02789 (accessed November 20, 2022).",
"C.-Y. Weng, B. Curless, P.P. Srinivasan, J.T. Barron, I. Kemelmacher-Shlizerman, HumanNeRF: Free-viewpoint Rendering of Moving People from Monocular Video, (2022). http://arxiv.org/abs/2201.04127 (accessed November 20, 2022).",
"Y. Jiang, S. Jiang, G. Sun, Z. Su, K. Guo, M. Wu, J. Yu, L. Xu, NeuralHOFusion: Neural Volumetric Rendering under Human-object Interactions, (2022). http://arxiv.org/abs/2202.12825 (accessed November 20, 2022).",
"T. Xu, Y. Fujita, E. Matsumoto, Surface-Aligned Neural Radiance Fields for Controllable 3D Human Synthesis, (2022). http://arxiv.org/abs/2201.01683 (accessed November 20, 2022).",
"L. Song, X. Gong, B. Planche, M. Zheng, D. Doermann, J. Yuan, T. Chen, Z. Wu, PREF: Predictability Regularized Neural Motion Fields, (2022). http://arxiv.org/abs/2209.10691 (accessed November 20, 2022).",
"	S. Wang, K. Schwarz, A. Geiger, S. Tang, ARAH: Animatable Volume Rendering of Articulated Human SDFs, (2022). http://arxiv.org/abs/2210.10036 (accessed November 20, 2022).",
"	Z. Zheng, H. Huang, T. Yu, H. Zhang, Y. Guo, Y. Liu, Structured Local Radiance Fields for Human Avatar Modeling, in: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), IEEE, New Orleans, LA, USA, 2022: pp. 15872–15882. https://doi.org/10.1109/CVPR52688.2022.01543.",
"	W. Jiang, K.M. Yi, G. Samei, O. Tuzel, A. Ranjan, NeuMan: Neural Human Radiance Field from a Single Video, (2022). http://arxiv.org/abs/2203.12575 (accessed November 20, 2022).",
"		S.-Y. Su, T. Bagautdinov, H. Rhodin, DANBO: Disentangled Articulated Neural Body Representations via Graph Neural Networks, (2022). http://arxiv.org/abs/2205.01666 (accessed November 20, 2022).",
"	C. Wang, M. Chai, M. He, D. Chen, J. Liao, CLIP-NeRF: Text-and-Image Driven Manipulation of Neural Radiance Fields, (2022). http://arxiv.org/abs/2112.05139 (accessed November 20, 2022).",
"	K. Kania, K. Moo Yi, M. Kowalski, T. Trzciniski, A. Tagliasacchi, CoNeRF: Controllable Neural Radiance Fields, in: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), IEEE, New Orleans, LA, USA, 2022: pp. 18602–18611. https://doi.org/10.1109/CVPR52688.2022.01807.",
"	Y.-J. Yuan, Y.-T. Sun, Y.-K. Lai, Y. Ma, R. Jia, L. Gao, NeRF-Editing: Geometry Editing of Neural Radiance Fields, (2022). http://arxiv.org/abs/2205.04978 (accessed November 20, 2022).",
"	T. Xu, T. Harada, Deforming Radiance Fields with Cages, (2022). http://arxiv.org/abs/2207.12298 (accessed November 20, 2022).",
"	Q. Wu, X. Liu, Y. Chen, K. Li, C. Zheng, J. Cai, J. Zheng, Object-Compositional Neural Implicit Surfaces, (2022). http://arxiv.org/abs/2207.09686 (accessed November 20, 2022).",
"	Y.-L. Qiao, A. Gao, M.C. Lin, NeuPhysics: Editable Neural Geometry and Physics from Monocular Videos, (2022). http://arxiv.org/abs/2210.12352 (accessed November 20, 2022).",
"	Y. Peng, Y. Yan, S. Liu, Y. Cheng, S. Guan, B. Pan, G. Zhai, X. Yang, CageNeRF: Cage-based Neural Radiance Field for Generalized 3D Deformation and Animation, (n.d.) 20.",
"	S. Kobayashi, E. Matsumoto, V. Sitzmann, Decomposing NeRF for Editing via Feature Field Distillation, (2022). http://arxiv.org/abs/2205.15585 (accessed November 20, 2022).",
"	J. Tang, X. Chen, J. Wang, G. Zeng, Compressible-composable NeRF via Rank-residual Decomposition, (2022). http://arxiv.org/abs/2205.14870 (accessed November 20, 2022).",
"	N. Müller, A. Simonelli, L. Porzi, S.R. Bulò, M. Nießner, P. Kontschieder, AutoRF: Learning 3D Object Radiance Fields from Single View Observations, (2022). http://arxiv.org/abs/2204.03593 (accessed November 21, 2022).",
"	A. Kundu, K. Genova, X. Yin, A. Fathi, C. Pantofaru, L. Guibas, A. Tagliasacchi, F. Dellaert, T. Funkhouser, Panoptic Neural Fields: A Semantic Object-Aware Neural Scene Representation, (2022). http://arxiv.org/abs/2205.04334 (accessed November 21, 2022).",
"	M. Boss, A. Engelhardt, A. Kar, Y. Li, D. Sun, J.T. Barron, H.P.A. Lensch, V. Jampani, SAMURAI: Shape And Material from Unconstrained Real-world Arbitrary Image collections, (2022). http://arxiv.org/abs/2205.15768 (accessed November 20, 2022).",
"	M. Tancik, V. Casser, X. Yan, S. Pradhan, B. Mildenhall, P.P. Srinivasan, J.T. Barron, H. Kretzschmar, Block-NeRF: Scalable Large Scene Neural View Synthesis, (2022). http://arxiv.org/abs/2202.05263 (accessed November 20, 2022).",
"	H. Turki, D. Ramanan, M. Satyanarayanan, Mega-NeRF: Scalable Construction of Large-Scale NeRFs for Virtual Fly- Throughs, in: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), IEEE, New Orleans, LA, USA, 2022: pp. 12912–12921. https://doi.org/10.1109/CVPR52688.2022.01258.",
"	K. Rematas, A. Liu, P. Srinivasan, J. Barron, A. Tagliasacchi, T. Funkhouser, V. Ferrari, Urban Radiance Fields, in: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), IEEE, New Orleans, LA, USA, 2022: pp. 12922–12932. https://doi.org/10.1109/CVPR52688.2022.01259.",
"	Y. Xiangli, L. Xu, X. Pan, N. Zhao, A. Rao, C. Theobalt, B. Dai, D. Lin, BungeeNeRF: Progressive Neural Radiance Field for Extreme Multi-scale Scene Rendering, (2022). http://arxiv.org/abs/2112.05504 (accessed November 20, 2022)."]

str='H. Wang, J. Ren, Z. Huang, K. Olszewski, M. Chai, Y. Fu, S. Tulyakov, R2L: Distilling Neural Radiance Field to Neural Light Field for Efficient Novel View Synthesis, (2022). http://arxiv.org/abs/2203.17261 (accessed November 20, 2022).'
for i in range(5,len(str_list)) :
    driver = webdriver.Edge(executable_path=r'C:\Users\zjh\PycharmProjects\批量文献自动转换器\msedgedriver.exe')
    driver.get(r'https://gfsoso.99lb.net/')
    driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/center[1]/div[4]/form[1]/div[1]/input[1]').send_keys(str_list[i].lstrip())#str_list[i].lstrip()左边有空格不行
    driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/center[1]/div[4]/form[1]/div[2]/input[1]').click()

    list_windows = driver.window_handles
    driver.switch_to.window(list_windows[1])
    sleep(5)
    try:
        driver.find_element(By.XPATH,"//a[@class='close']").click()
        driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[10]/div[2]/div[3]/div[2]/div[1]/div[2]/div[3]/a[2]/span[1]').click()
        sleep(5)
        text=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[1]/table/tbody/tr[1]/td/div').text
        print(text)
    except:
        print("第",i,"条数据失败",str_list[i].lstrip())
    driver.close()