# regolith.pdf

- document_id: `b379e8689263dc6d`
- sha256: `b379e8689263dc6d717eab15804de48388ede24f899f7e35dd0981839a72fdc5`
- page_count: 16

## Page 1

Microscopy and Microanalysis, 2026, 32, ozag013 
 https://doi.org/10.1093/mam/ozag013 
 Advance access publication 13 March 2026 
 Original Article 
 
 
 Statistical Analysis and Modeling of the 3D Morphology and 
 
 Texture of Lunar Regolith Simulants 
 
 Matthias Weber1,* , Ralf Ditscherlein2 , Lisa Ditscherlein2, Tehya Birch3, Markus Franz3,
 Achim Seidel3, Urs A. Peuker2, Orkun Furat1,4, Volker Schmidt1 , and Georg Pöhle5
 1Institute of Stochastics, Ulm University, Helmholtzstr. 18, Ulm 89081, Germany
 2Institute for Mechanical Process Engineering and Mineral Processing, TU Bergakademie Freiberg, Agricolastr. 1, Freiberg 09599, Germany
 3Airbus Defence and Space, Claude Dornier Str., Immenstaad 88090, Germany 
 4Applied AI and Data Science Unit, University of Southern Denmark, Campusvej 55, Odense 5230, Denmark
 5Fraunhofer Institute for Manufacturing Technology and Advanced Materials IFAM, Winterbergstr. 28, Dresden 01277, Germany
 *Corresponding author: Matthias Weber, E-mail: matthias.weber@uni-ulm.de 
 Abstract 
 Understanding the mechanical behavior of lunar regolith under low-g conditions is essential for processing regolith in the lunar environment. While
 well understood for many granular materials on Earth, these properties have yet to be studied for lunar regolith. For ground-based experimental
 investigation of regolith properties, simulants are used, which mimic certain physical or chemical aspects of lunar regolith. However, rheology is
 significantly influenced by particle size and shape, which has not yet been thoroughly characterized for lunar regolith particles. Moreover, it
 remains unclear how well common simulants approximate the morphology of lunar regolith particles. In this paper, we quantify the
 multivariate distributions of size and shape descriptors of actual lunar regolith particles and seven commonly used mare and highlands regolith
 simulants, using 3D tomographic image data obtained via micro computed tomography. Quantitative analysis confirms that there are large
 differences in morphology within regolith simulants and between simulants and lunar regolith. This highlights the need to develop regolith
 simulants with accurate morphologies for experimental investigations of mechanical properties. Alternatively, statistically representative
 digital models of lunar regolith can be used as input for numerical simulations, enabling simulation studies of morphology-driven mechanical
 behavior under lunar conditions. 
 Key words: 3D image data, X-ray micro-CT, regolith simulant, particle descriptor, parametric stochastic model
 Introduction regolith will play a pivotal role. The Mini-ROXY mission
 exemplifies this focus as regolith handling involves significant
 Space exploration activities are expected to grow significantly 
 challenges, including clogging and flow inconsistencies in trans-
 over the next decades as evidenced by current trends and numer- 
 port and storage systems, which could jeopardize mission suc-
 ous roadmaps presented at national and global levels, beginning 
 cess. These issues arise from the unique and complex behavior
 with the International Space Station and continuing to the lunar 
 of regolith under lunar conditions, where extreme temperature
 vicinity, the Moon, asteroids and Mars (Seidel et al., 2022). This 
 variations, reduced gravity and electrostatic interactions influ-
 trend is fueled by advancements in technology and, in particular, 
 ence its rheological and mechanical properties. One key object-
 decreasing launch costs. Central to these ambitions is the con- 
 ive of the Mini-ROXY lunar demonstration mission is therefore
 cept of In-Situ Resource Utilization (ISRU), or “living off the 
 to improve our understanding of the behavior of lunar regolith
 land,” which emphasizes the production of essential resources 
 in dynamical situations. This general approach, which has been
 such as oxygen and metals locally rather than supplying them 
 coined UPREB (Universal Predictors of Regolith Behavior)
 from Earth. These resources are critical for life support, fuel pro- 
 duction, construction, and other applications (Laurini & (Birch et al., 2025), will help to fully exploit the potential of
 Gerstenmaier, 2014; Seidel et al., 2022). ISRU activities are regolith for ISRU and further applications on the Moon and,
 expected to grow to a market of 63 billion dollars by 2040, pre- with suitable adaptations, even beyond. The overarching ques-
 dominantly driven by oxygen production from local resources. tion is how regolith behaves when being handled, mobilized,
 The ROXY (Regolith to Oxygen and Metals Conversion) processed and transported on the lunar surface in partial gravity
 molten salt electrolysis process developed by Airbus meets the and in the lunar environment. Understanding these properties,
 requirements for an economically viable ISRU process to extract namely, the rheology of lunar regolith, is crucial for predicting
 oxygen and metals from regolith (Haeming et al., 2020; Seidel how regolith can be handled and processed for scientific experi-
 et al., 2021, 2022). A lunar demonstration mission with a mini- ments and ISRU.
 aturized version of a ROXY reactor, called Mini-ROXY, is cur- A crucial component of this understanding is the quantita-
 rently in preparation (Seidel et al., 2023). tive characterization of particle morphology. The distribu-
 As ISRU and lunar exploration efforts progress (Deng et al., tions of morphological and textural descriptors of regolith
 2025; Li et al., 2025), the handling and processing of lunar particles govern mechanical properties and flow behavior.
 Received: October 23, 2025. Revised: January 30, 2026. Accepted: February 17, 2026
 © The Author(s) 2026. Published by Oxford University Press on behalf of the Microscopy Society of America.
 This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which
 permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
## Page 2

2 Microscopy and Microanalysis, 2026, Vol. 32, No. 2
 
 Accurate quantification of morphology thus represents an essen- particular, it is well established for various other materials
 tial step toward predicting mechanical behavior of regolith and that their mechanical behavior on Earth typically depends
 facilitates reliable design of equipment and risk assessment for on numerous influencing descriptors for their size, shape, sur-
 ISRU applications. face roughness and composition (Spettl et al., 2016). For par-
 Despite research progress (Tute & Goulas, 2024; Zanon ticle systems, these descriptors are typically random, making
 et al., 2024; Pourakbar et al., 2025; Tsuchiyama et al., 2025), their characterization naturally suited to probability distribu-
 substantial knowledge gaps remain in understanding the rhe- tions. However, different types of descriptors are often corre-
 ology of lunar regolith (Azami et al., 2024). Large-scale experi- lated (e.g., when shape depends on size), meaning that
 mental investigations of mechanical properties of regolith are describing them solely with univariate distributions results in
 currently unfeasible on the Moon and reproducing lunar condi- a significant loss of information. To capture the full complex-
 tions on the Earth requires elaborate experimental setups, e.g., ity of these interdependencies, it is essential to utilize multi-
 parabolic flights or drop towers. Additionally, large quantities variate probability distributions, which can account for the
 of lunar regolith are unavailable for mechanical experiments relationships and interactions among the descriptors, provid-
 and while lunar regolith simulants exist, their applicability for ing a more comprehensive and accurate statistical representa-
 such experiments is questionable. tion of the particle properties. 
 In the past, the analysis of lunar regolith has focused on its Additionally, univariate or multivariate distributions of mor-
 chemical and mineralogical composition and properties (Sibille phological particle descriptors are useful targets for the develop-
 et al., 2006; Martin & Wagoner, 2022). In order to mimic lunar ment of a digital twin for the 3D morphology of lunar regolith
 regolith in that regard, various types of regolith simulants (Li particles, i.e., for developing stochastic 3D models from which
 et al., 2022) have been developed. Additionally, mechanical virtual, but realistic regolith particles can be generated for the
 properties of regolith simulants have been investigated (Otto purpose of virtual materials testing. While matching the precise
 et al., 2018). However, it remains unclear whether regolith sim- shapes of individual particles could be considered overfitting of
 ulants are representative for lunar regolith with respect to their the stochastic 3D model, fitting of univariate distributions of in-
 mechanical properties, as these are not only influenced by min- dividual morphological particle descriptors or, even better,
 eralogical properties but also by the size and shape of regolith multivariate distributions can be used for assessing the perform-
 particles. While these relationships are well understood for ance of a stochastic 3D model for particle sizes, shapes and com-
 many granular materials and mechanical processes on Earth position (Prifling et al., 2019).
 (Schulze, 2021), the shapes of lunar regolith particles have only In the present paper, multivariate statistical analysis and
 been analyzed for single (Baidya et al., 2022) or a small number parametric models for multivariate non-Gaussian probability
 of particles in the past (Katagiri et al., 2015; Tsuchiyama et al., distributions of descriptor vectors are used to better understand
 2022). Due to these concerns and constraints on experimental de- similarities and differences of regolith simulant particles. We
 signs, regolith simulants may be insufficient to reliably predict the apply these methods to 3D X-ray micro-CT data of different
 mechanical behavior of actual regolith under lunar conditions. regolith simulants representing mare and highlands regolith.
 This gap may be bridged by numerical simulations applied to Additionally, we compare these simulants to three different
 a digital twin of the 3D morphology and mineralogical com- samples of lunar regolith, highlighting the necessity for a thor-
 position of lunar regolith particles. Such a digital twin of lunar ough investigation of the shapes of lunar regolith particles to
 regolith can be obtained by stochastic 3D modeling of the shape better understand their mechanical behavior.
 and inner composition of regolith particles, based on 
 highly-resolved image data which are gained by computed tom- Materials and Methods
 ography (CT). Investigating material properties by the combin- 
 In the following, we introduce the materials and methods used
 ation of a digital twin and numerical simulations is known as 
 throughout this paper, including the regolith simulants, meas-
 virtual materials testing and has been successfully applied to 
 urement techniques and considered particle descriptors.
 various other materials (Neumann et al., 2018; Jung et al., 
 2022; Weber et al., 2024). For developing a realistic digital 
 twin of lunar regolith, a better understanding of the 3D morph- Regolith Simulants
 ology and texture of lunar regolith particles is required. For analysis by X-ray CT, we chose four different mare and
 In addition to the 2D characterization of statistically three different highland types of regolith simulants. Table 1
 relevant quantities (Isachenkov et al., 2022), 3D X-ray micro- shows the different mineralogical compositions of these mate-
 and nano-CT measurements of large numbers of particles rials according to the manufacturer.
 from samples of lunar regolith from the Apollo 11 and 
 Apollo 14 missions (Chiaramonti & Garboczi, 2024) and, 
 most recently, the Chang’e-5 mission (Wu et al., 2025), have Table 1. Mineralogical Composition (wt.%) of Regolith Simulants.
 only recently been performed and analyzed (Goguen et al., 
 Name Type Glass Plag Ol Px Bas Ilm 
 2024; Kafka et al., 2025). In contrast to lunar regolith, 
 many studies of regolith simulants are also limited to the inves- CSM-LHT-1 h – 70.0 – – 30.0 –
 OB1A h 43.2 44.4 6.3 0.6 – – 
 tigation of a single regolith simulant (Peng et al., 2023) and 
 LHS-1 h 24.2 74.4 0.2 0.3 0.5 0.4 
 therefore do not allow direct comparisons of inherent proper- 
 JSC-1A m 49.3 37.1 9.0 – – – 
 ties between different simulants. LMS-1 m 32.0 19.8 11.1 32.8 – 4.3 
 In addition to the analysis of univariate descriptors of par- OPRL2N m 90.0 10.0 – – – –
 ticle shape as discussed in (Goguen et al., 2024), a multivariate CSM-LMT-1 m – – 10.0 – 86.0 4.0
 analysis, incorporating information of chemical composition 
 The considered mineralogical phases, ordered from lowest to highest X-ray
 obtained from the raw CT data, will prove beneficial for a bet- 
 attenuation are: Plag=Plagioclase, Ol=Olivine, Px=Pyroxene,
 ter understanding of regolith properties and behavior. In Bas=Basalt, Ilm=Ilmenite, m=Mare, h=Highland.
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
## Page 3

Matthias Weber et al. 3 
 
 For further analysis, in particular when using X-ray CT, only cathode to a target anode (e.g., tungsten), generate X-rays. The
 a limited range of particles sizes can be observed at the same interaction within the target creates a bulb-shaped volume, pro-
 time. Thus, in a first step, we chose to sieve all samples to ducing two types of X-rays. One of them are characteristic
 <250μm. Table 2shows information on the particle size distri- X-rays, determined by the target material, which are primarily
 bution after sieving determined with laser diffraction (Malvern, useful for chemical analysis but irrelevant here, since the min-
 Mastersizer 3000). For the actual CT measurements, we add- eralogical composition of the target material is known. The oth-
 itionally removed the fines below 25μm by wet sieving. Note er one is bremsstrahlung, a continuous spectrum influenced by
 that the size interval of the middle fraction from 25μm to filtering and electron acceleration voltage, which determines
 250μm is commonly used in other studies as well and is a the main part of the integral spectrum used for the measure-
 trade-off between practical imaging constraints (like the min- ments. Here, the stability of the X-ray interaction bulb is critical
 imum number of voxels for a reasonable description of particle for sharp and reproducible imaging. The conical X-ray beam
 shape). However, this selection may lead to bias. Finer and passes through the sample, projecting onto a 2D flat panel de-
 coarser particles often differ in shape and composition, which tector. Unlike medical CT, the sample rotates while the detector
 may affect the overall trends. Therefore, our results, and com- remains fixed. Each rotational step produces a projection image,
 parable studies as well, represent only part of the particle size forming a series of 2D projection images to be processed into a
 distribution, and caution should be taken when generalizing. 3D tomogram using reconstruction algorithms such as filtered
 Following studies will include correlative measurements for back projection (FBP). For more details, we refer e.g., to
 evaluating excluded fractions. (Buzug, 2008). Exemplary particles of the regolith simulants
 in Table 2 measured via X-ray tomography are visualized in
 Acquisition and Processing of Image Data Figure 1, where it is clearly visible that the particles show large
 variations in shape and surface modifications.
 The acquisition and processing of image data considered in 
 In order to make the measurements of the regolith simulant
 this paper consists of three steps: particle-discrete sample 
 samples, i.e., their gray value distributions, as comparable as
 preparation, X-ray tomographic measurements, and data pre- 
 possible, the measurement parameters were kept constant
 processing and segmentation. 
 (Xradia 510 VERSA by ZEISS, Germany, sample diameter:
 2 mm, acceleration voltage: 80 keV, beam power: 7 W, expos-
 Particle-Discrete Sample Preparation 
 ure time: 1.5 s, binning: 2, filter: Zeiss standard LE4). Figure 2
 The basis for multivariate statistical data analysis is a set of 
 shows exemplary slices from the seven regolith simulants.
 particle-discrete morphological and textural descriptors of rego- 
 A standardization of the gray values is needed to enable a
 lith simulants. To avoid time-consuming post-processing of im- 
 quantitative analysis. This can only be done by utilizing correla-
 age data prior to segmentation into individual particle volumes, 
 tive methods such as scanning electron microscopy (SEM) com-
 an adapted sample preparation workflow was used that keeps 
 bined with energy-dispersive X-ray spectroscopy (EDX), which
 the regolith particles at a distance. Here, the well–known immo- 
 is possible on the micrometer (Schulz et al., 2020) and sub-
 bilization through epoxy embedding was complemented by 
 micrometer scale (Englisch et al., 2023). However, these methods
 introducing weakly X-ray absorbing carbon black spacer par- 
 are limited to 2D measurements and cannot be carried out
 ticles in the nanometer size range—much below the actual iso- 
 without further sample preparation. State-of-the-art spectral
 tropic voxel resolution of (2.3μm)×(2.3μm)×(2.3μm)—to 
 CT scanners can do this also in the 3D volume of the sample
 avoid agglomerates and sedimentation effects, which cannot 
 (Sittner et al., 2020), but not yet with the resolution required
 be neglected in the present size and mass density range of the 
 here and, due to the large amount of data, not yet for a large num-
 particles (Ditscherlein et al., 2022). 
 ber of densely packed samples with a large number of particles.
 To nevertheless create a valid starting point for gray value evalu-
 X-ray Tomographic Measurements 
 ation, all regolith samples were scanned and examined for the
 Non-destructive X-ray tomographic measurements have be- most highly absorbing phase, which represents the upper limit
 come a standard characterization method in recent years of the normalization condition. The other data sets were then re-
 (Withers et al., 2021), especially when characterizing particulate constructed from the raw data within the new limits. Given a sta-
 systems (Lin & Miller, 2005). A typical lab-based X-ray system ble X-ray source and short consecutive measurements, the gray
 uses a polychromatic source where electrons, accelerated from a values can then be quantitatively compared with each other.
 Data Pre–Processing and Segmentation 
 Table 2. Grain Density ρ, and Quantiles d10,d50,d90 of the Particle Size 
 Distribution (sieved Below 250μm, Determined with Laser Diffraction) For discrete particle segmentation, a two-step supervised
 for Mare (top Three) and Highland (bottom Four) Regolith Simulants, Ilastik training algorithm (Berg et al., 2019) was used, starting
 Where the Following Abbreviations are Used: CSM = Colorado School of with the creation of a pixel classifier. In this step, the material
 Mines, EL = Exolith Lab, DI = Deltion Innovations Ltd., OPR = Off Planet phase is separated from the background phase (see Fig. 3). In
 Research. 
 the next step, an automated routine processes the entire image
 Name Manufacturer ρ d 10 d 50 d 90 stack, identifying individual volumes of the material phase and
 (g/cm3) (μm) (μm) (μm) assigning them distinct colors. These color codes are then con-
 CSM-LHT-1 CSM 2.85 4.2 51.7 216.8 verted into unique gray values, referred to as labels, which are
 LHS-1 EL 3.30 9.9 82.9 234.7 utilized in a second object-classifier routine to extract quanti-
 OB1A DI 3.03 18.9 80.3 185.2 tative data. However, for particle-discrete analysis of the ma-
 JSC-1A ORBITEC 2.90 18.1 74.9 233.2 terial phase distribution, it is crucial that the information
 LMS-1 EL 2.92 11.9 88.7 240.5 
 about an aggregated gray value or histogram is preserved for
 OPRL2N OPR 2.85 3.8 31.2 156.5 
 each particle. This can be done by reusing the generated par-
 CSM-LMT-1 CSM 2.90 4.7 54.8 206.7 
 ticle labels in combination with the original image data.
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
### Equation candidates
- `p0003_eq_004`: < 250 μ m. Table 2 shows information on the particle size distri- X-rays, determined by the target material, which are primarily
  - crop: `regolith_b379e8689263dc6d/assets/equations/page_0003_equation_004.png`

## Page 4

4 Microscopy and Microanalysis, 2026, Vol. 32, No. 2
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Fig. 1. 3D models of selected particles (150μm to 250μm) from regolith simulants in Tab. 2illustrating the diversity in shape and surface texture. A scale
 bar is omitted, as the models are not rendered isometrically and are intended for qualitative visualization only.
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Fig. 2. Exemplary slices of tomographically reconstructed samples of the regolith simulants in Table 2, measured via X-ray tomography. Highly X-ray
 attenuating phases are brighter, whereas less attenuating phases are darker. Spherical black areas are air bubbles due to the sample preparation
 procedure, which can later be used as markers for correlative scans. 
 Particle Descriptors vulnerability to clogging and sieving behavior. Additionally,
 The regolith simulants are analyzed with respect to different texture observed in CT images is analyzed as this relates to their
 particle-discrete descriptors. In particular, descriptors of par- chemical and mineralogical composition and, thereby, electro-
 ticle size and shape as well as such of texture are investigated, static properties. All particle descriptors considered in this pa-
 where the shapes of particles can be directly related to various per are computed directly from the voxelized image-data
 rheological properties of bulk regolith like flowability, representation of particles described in the previous sections.
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
### Figure / graphic candidates
- `p0004_figure_000`: Fig. 2. Exemplary slices of tomographically reconstructed samples of the regolith simulants in Table 2, measured via X-ray tomography. Highly X-ray
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0004_figure_000.png`
- `p0004_figure_001`: No caption detected
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0004_figure_001.png`

## Page 5

Matthias Weber et al. 5 
 
 
 
 
 
 
 
 
 
 
 
 
 Fig. 3. Exemplary reconstructed slice from the OB1A dataset with magnified region showing markers for the particle (yellow) and background phase
 (blue) to train the pixel-based classifier with Ilastik giving a segmented image (visual validation showing no missing particles) that can be used for an
 object-based classifier assigning a distinct false color map. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Fig. 4. Histograms of particle sizes obtained for laser-diffraction data (green), for volume-equivalent spheres extracted from CT images (orange), and for
 Feret diameters (blue), for the regolith simulants CSM-LHT-1 (left) and JSC-1A (right).
 
 Morphological Descriptors Textural Descriptors 
 The most fundamental descriptors of particle morphology are the As described previously, the CT measurements of different simu-
 volume V and surface area A of a particle, where the particle vol- lants were performed with the aim of preserving comparability of
 ume is simply calculated by counting the voxels associated with gray values between different samples. Thus, besides morphologic-
 that particle. The surface area is computed by the algorithm pro- al descriptors, meaningful descriptors of regolith particle texture
 posed in (Schladitz et al., 2007), which is based on a convolution can be computed for comparisons within and between simulants.
 of the image with a 2×2×2 kernel and thus avoids the recon- Since electrostatic charging, as one of the main phenomena of
 struction of the actual surface while yielding more accurate results interest, is particularly related to the composition of particle sur-
 compared to simply counting voxels which touch both the inter- faces, we split each particle into two parts: interior and surface.
 ior and exterior of a particle. The latter would introduce a signifi- For this purpose, to avoid partial volum√e�� effects, we only consider
 cant bias depending on the voxel-resolution of the measurement. voxels with a distance of more than 3voxels (≈4μm) to the
 A commonly used descriptor of particle shape, being a b√o��undary √of�� particles. Then, all voxels with a distance between
 measure of roundness, is the so-called sphericity S of a particle, 3and 2 3voxels to the particle boundary are considered as
 which is given by su√rf��ace voxels, whereas voxels with a distance of more than
 2 3voxels to the boundary are considered as interior voxels.
 π(6V)2/3 
 In the following, by G , G and G, the sets of gray values are
 S= . s i t 
 3A denoted associated with surface, interior and all voxels of a
 particle, respectively, where the particle-wise mean gray value
 Additionally, the aspect ratio R of particles is considered, which 
 μ(G ) and coefficient of variation cv(G ) are computed for
 is given as the ratio of the lengths of the longest and shortest x x 
 each x∈{s,i,t}. Note that the quantities μ(G ) and μ(G) are
 principal axes of an ellipsoid with the same normalized second s i 
 related with the average composition of the particle surface
 central moments as the particles. To compute the aspect ratio, 
 and interior, respectively, whereas cv(G) and cv(G) charac-
 the measure.regionprops method from the python pack- s i 
 terize the heterogeneity of these sub-volumes of a particle.
 age scikit-image (Van der Walt et al., 2014) is used. Like spher- 
 icity, the aspect ratio R quantifies the roundness of particles, but 
 is not affected by, e.g., surface roughness. Finally, we compute Stochastic Modeling of Particle Descriptor Vectors
 the Feret diameter D , i.e., the maximum distance between To quantitatively compare the regolith simulants stated in
 F 
 two parallel planes tangent to the particle surface. Tables 1 and 2, we fit multivariate probability distributions
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
### Figure / graphic candidates
- `p0005_figure_000`: Fig. 3. Exemplary reconstructed slice from the OB1A dataset with magnified region showing markers for the particle (yellow) and background phase
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0005_figure_000.png`
- `p0005_figure_001`: Fig. 3. Exemplary reconstructed slice from the OB1A dataset with magnified region showing markers for the particle (yellow) and background phase
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0005_figure_001.png`

## Page 6

6 Microscopy and Microanalysis, 2026, Vol. 32, No. 2
 
 to vectors of morphological and textural particle descriptors, vectors. So-called copulas (Nelsen, 2006) offer this flexibility
 which have been introduced in the previous section. This is by allowing to separately model the univariate (marginal) dis-
 done in two steps. First, we consider univariate probability tributions and the correlation structure of a multivariate
 distributions of single particle descriptors. Then, the univari- distribution.
 ate distributions are combined into a multivariate probability For any fixed integer d>1, a d-variate copula is the cumu-
 distribution of particle descriptor vectors, where the concept lative distribution function C:[0,1]d →[0,1] of a
 of copulas is used. d-dimensional random vector with uniform marginal distribu-
 tions on [0,1]. Furthermore, Sklar’s representation formula
 Univariate Distributions (Nelsen, 2006; Joe, 2014) motivates the use of copulas for
 the parametric modeling of (non-Gaussian) multivariate dis-
 A first step towards parametric modeling the (non-Gaussian) 
 tributions, by stating that for any d-variate distribution func-
 multivariate distributions of particle descriptor vectors is a 
 tion F:Rd →[0,1] with marginal distribution functions
 parametric representation of the univariate distributions of in- 
 F , ...,F :R→[0,1], there is a copula C such that
 dividual descriptors. For this, we consider various parametric 1 d 
 families of univariate probability distributions which can be F(x , ...,x )=C(F (x ), ...,F (x )), (3)
 1 d 1 1 d d 
 fitted to the data, where the best-fitting distribution family is 
 chosen either among those implemented in the scipy package for all x 1 , ...,x d ∈R. Note that the formula given in
 (Virtanen et al., 2020) or, alternatively, as a Gaussian mixture Equation (3) implies that the corresponding d-variate prob-
 model. This choice of candidates may be adjusted, e.g., when ability density f:Rd →[0,∞) can be given by
 prior knowledge about the expected distribution families is 
 f(x , ...,x )=c(F (x ), ...,F (x ))f (x )...f (x ), (4)
 available for specific descriptors. 1 d 1 1 d d 1 1 d d 
 Two notable parametric distribution families which will be for all x , ...,x ∈R, where f :R→[0,∞) is the (univariate)
 1 d i 
 used in this paper are a version of the generalized inverse probability density corresponding to F for i∈{1, ...,d}, and
 i 
 Gaussian distribution, whose probability density f gig :R→ c:[0,1]d →[0,∞) is the (d-variate) probability density corre-
 [0,∞) can be defined as sponding to the copula C:[0,1]d →[0,1]. 
 f (x;p,b)=xp−1exp(−b(x+1/x)/2)/(2K (b)) (1) Among other parametric copula families, so-called
 gig p 
 Archimedean copulas are often considered in the literature
 for each x∈R and some parameters p∈R,b>0, see (Nelsen, 2006; Joe, 2014). For a continuous, strictly decreas-
 (Barndorff-Nielsen et al., 1978), and the normal inverse ing convex function ψ:[0,1]→[0,∞) with ψ(1)=0, an
 Gaussian distribution with probability density f nig :R→ Archimedean copula C:[0,1]d →[0,1] is defined as
 [0,∞) given by 
 √�������� C(u 1 , ...,u d )=ψ−1(ψ(u 1 )+...+ψ(u d )), (5)
 aK (a 1+x2) √��������� 
 f nig (x;a,b)= 1√�������� exp( a2−b2+bx) (2) for all u 1 , ...,u d ∈[0,1], where the function ψ on the right-
 π 1+x2 hand side of Equation (5) is called the generator function of
 for each x∈R and some parameters a>0,|b|≤a, where the Archimedean copula and ψ−1 is the pseudo-inverse of ψ.
 K :[0,∞)→[0,∞) is a modified Bessel function of the se- Two examples of Archimedean copulas which will be used
 p 
 cond kind. in this paper are the so-called BB1 and BB8 copulas, as they
 Note that the distribution families given in Equation (1) and turn out to best fit the data at hand. Their generators
 (2) can be transformed linearly by additionally introducing so- ψ ,ψ :[0,1]→[0,∞) are given by
 BB1 BB8 
 called location and scale parameters l∈R and s>0. For any 
 probability density f:R→[0,∞), the transformed density ψ BB1 (u;a,b)=(u−a−1)b (6)
 f l,s :R→[0,∞) is then given by f l,s (x)=f((x−l)/s)/s for and 
 each x∈R. 􏼠 􏼡 
 Furthermore, as parametric model for a univariate bimodal 1−(1−δu)θ 
 ψ (u;θ,δ)=log , (7) 
 distribution, we consider the Gaussian mixture model, whose BB8 1−(1−δ)θ 
 probability density f :R→[0,∞) is given by 
 GMM 
 for each u∈[0,1] and some parameters a>0,b≥1 and
 f GMM (x;p,μ 1 ,μ 2 ,σ 1 ,σ 2 ) θ≥1,0<δ≤1. 
 =pφ((x−μ )/σ )/σ +(1−p)φ((x−μ )/σ )/σ , In the case of a bivariate copula C:[0,1]2 →[0,1], so-
 1 1 1 2 2 2 
 called rotations C ,C ,C :[0,1]2 →[0,1] of the cop-
 for each x∈R, where φ:R→[0,∞) is the probability density 90 180 270 
 ula C are defined for angles of 90◦, 180◦ and 270◦ by
 of the standard normal distribution, p∈[0,1] is the mixing 
 C (u ,u )=C(u ,1−u ), C (u ,u )=C(1−u ,1−u )
 parameter, and μ ,μ ∈R and σ ,σ are the mean values and 90 1 2 2 1 180 1 2 1 2
 1 2 1 2 and C (u ,u )=C(1−u ,u ) for any u ,u ∈[0,1]. For
 standard deviations of the mixing components, respectively. 270 1 2 2 1 1 2 
 parametric copula families, allowing such rotations leads to
 a broader range of feasible copula structures.
 Archimedean Copulas 
 While the univariate distributions of single particle descriptors 
 can be modeled by means of simple parametric distribution R-Vine Copulas 
 families, as stated in the previous section, the joint (multivari- Archimedean copulas, and an even wider range of other para-
 ate) distributions of descriptor vectors in general do not follow metric copula families, are well-suited for modeling two-
 an established modeling scheme like, e.g., a multivariate dimensional correlation structures. However, most of them
 Gaussian distribution. Thus, a more flexible approach is fail to capture the complexity of higher-dimensional distribu-
 needed to model the joint distribution of particle descriptor tions. To overcome these limitations, so-called R-vine copulas
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by guest
 on 
 24 
 April
 2026
## Page 7

Matthias Weber et al. 7 
 
 (Joe, 2014; Czado, 2019) have been developed that provide This data contains all segmented particles as discussed in
 means of parametrically modeling multivariate distributions Section “Materials and Methods.” By computing the particle
 in arbitrary dimensions while providing increased flexibility descriptors as outlined there, we obtain a dataset which forms
 to model the correlation structure. the basis for the following statistical analysis of similarities
 R-vine copulas are based on the so-called pair-copula and differences of regolith simulants.
 approach, which we outline for d=3. Consider a three- 
 dimensional random vector X=(X ,X ,X ) with joint prob- 
 1 2 3 Univariate Data Analysis 
 ability density f:R3 →[0,∞), marginal densities 
 For putting the following analyses into perspective, recall that
 f ,f ,f :R→[0,∞) and corresponding (univariate) cumula- 
 1 2 3 during sample preparation, fines below 25μm and extremely
 tive distribution functions F ,F ,F :R→[0,1]. Using the 
 1 2 3 large particles with sizes above 250μm were removed which
 notions of conditional probability densities and conditional 
 may change bulk properties compared to the specifications
 cumulative distribution functions, the right-hand side of 
 of manufacturers. Thus, the following analysis should be con-
 Equation (4) can be re-written in the following form, see 
 sidered valid only for the measured fraction of particle sizes
 (Weber et al., 2022): For all (x ,x ,x )∈R3 such that 
 1 2 3 between 25μm and 250μm. Note that a small amount of par-
 f(x ,x ,x )>0, it holds that 
 1 2 3 ticles outside this range may still be present in the sample due
 f(x ,x ,x )=c (F (x ),F (x )) to the unavoidable inaccuracy of the sieving process.
 1 2 3 1,3∣X2=x2 1∣X2=x2 1 3∣X2=x2 3 
 We also remark that the probability densities used in the fol-
 ×c (F (x ),F (x ))c (F (x ),F (x ))f (x )f (x )f (x ), 
 1,2 1 1 2 2 2,3 2 2 3 3 1 1 2 2 3 3 lowing, e.g., in Figures 5and 6are not volume-weighted and,
 (8) therefore, they may not perfectly reflect the visual impression
 where c and c are the copula densities corresponding to obtained from Figure 2.
 1,2 2,3 
 the distributions of (X ,X ) and (X ,X ), respectively, and Figure 4shows the histograms of particle sizes as obtained
 1 2 2 3 
 c is that corresponding to the conditional distribution by laser diffraction, in comparison to histograms of particle
 o 1 f , 3 ( ∣ X X2= , x X 2 ) given that X =x . Furthermore, F denotes sizes computed from CT image data.
 1 3 2 2 i∣X2=x2 
 Some of the apparent differences between the histograms in
 the conditional distribution function of X given that 
 i 
 Figure 4 may stem from the differences between the applied
 X =x , for i=1,3. Usually, the simplifying assumption is 
 2 2 
 measurement techniques, a known issue when comparing re-
 made that c =c , i.e., the copula density c 
 1,3|2 1,3∣X2=x2 1,3∣X2=x2 
 sults obtained from laser diffraction with those of CT image
 does not depend on the specific value of X , see (Haff et al., 
 2 
 data (Erdoğan et al., 2007). However, in addition, different
 2010). Having in mind that 
 regolith simulants may contain hugely different amounts of
 F (x )=∫ x1 f 1,2 (x,x 2 ) dx fines which are present in the laser diffraction data but not
 1∣X2=x2 1 −∞ f (x ) in the samples used for CT imaging. 
 2 2 
 =∫ 
 x1 
 c (F (x),F (x ))f (x)dx 
 While measured samples and the original bulk material dif-
 −∞ 1,2 1 2 2 1 fer obviously with respect to the particle size distribution, fur-
 and, analogously, ther differences may exist which cannot be easily quantified.
 In particular, Figure 5visualizes probability densities of size
 f (x ,x) 
 F (x )=∫ x3 2,3 2 dx and shape descriptors, whereas the corresponding probability
 3∣X2=x2 3 −∞ f (x ) 
 2 2 densities of textural descriptors are shown in Figure 6.
 =∫ x2 c (F (x ),F (x))f (x)dx Table 3summarizes this analysis by providing the mean val-
 −∞ 2,3 2 2 3 3 
 ues of the probability densities shown in Figures 5and 6for all
 for any x ,x ∈R, which follows from Equation (4) with 
 1 3 descriptors and simulants. As manufacturers specify regolith
 d=2, the formula given in Equation (8) yields a suitable ap- 
 simulants with focus on different applications and, thus differ-
 proach for computing the joint probability density f:R3 → 
 ent compositions, it is not surprising that the mean values in
 [0,∞) of the three-dimensional random vector 
 the respective rows of Table 3 are quite different from each
 X=(X ,X ,X ), using (parametric) models for the (univari- 
 1 2 3 other, which will be discussed in more detail in the following
 ate) probability densities f , f and f and the bivariate copula 
 1 2 3 sections. 
 densities c , c and c . 
 1,3|2 1,2 2,3 
 By iteratively applying the pair-copula approach stated 
 Multivariate Data Analysis 
 above, representation formulas similar to that given in 
 Equation (8) can be obtained for any dimension d>3, where While the data analysis performed in Section “Univariate Data
 d-variate probability densities are expressed by univariate Analysis” was mainly focused on investigating similarities and
 probability densities and bivariate copula densities. differences between the distributions of single particle descrip-
 However, since in the present paper only trivariate copula tors, this study shall also serve as a first step towards stochastic
 models will be used, we will not elaborate further on the gen- 3D modeling of regolith particles as mentioned in the intro-
 eral construction of R-vine copulas for arbitrary dimensions duction. To this end, a better understanding of the correlations
 d>3 and refer to (Joe, 2014; Czado, 2019; Aigner et al., between different descriptors and of their joint multivariate
 2023; Furat et al., 2024) for further details. For fitting distributions is needed. While the following methods are ap-
 (R-vine) copulas to data, we will make use of the pyvinecopu- plicable to all simulants, we chose CSM-LHT-1 to demon-
 lib package (Vinecopulib, 2023). strate their capabilities, as this simulant exhibits some
 interesting correlations. 
 The Spearman rank correlation coefficients (Joe, 2014) of
 Results 
 the pairs of particle descriptors given in Figure 7show the ex-
 The image data considered in this paper refers to 189504 pected behavior. In particular, the volumes and surface areas
 individual particles of seven different regolith simulants. of particles are highly correlated. Aside from that, a strong
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
### Equation candidates
- `p0007_eq_006`: approach, which we outline for d = 3. Consider a three-
  - crop: `regolith_b379e8689263dc6d/assets/equations/page_0007_equation_006.png`

## Page 8

8 Microscopy and Microanalysis, 2026, Vol. 32, No. 2
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Fig. 5. Estimated probability densities of particle volume, surface area, sphericity and aspect ratio. Highland simulants are shown as dashed lines, mare
 simulants as solid lines. 
 
 negative correlation between volume (or surface area) and correlated (r =0.07), but their joint distribution shows
 s 
 sphericity exists, suggesting that larger particles are less round. some kind of dependence with respect to the particle volume,
 The aspect ratio, however, is not meaningfully correlated to as can be seen in Figure 8.
 neither volume nor surface area, so plate- or rod-shaped par- 
 ticles might come at all different sizes, see Section 
 “Discussion” for further details. Parametric Modeling of Univariate and Multivariate
 Figure 7shows that many particle descriptors are correlated Distributions 
 with each other. Thus, when investigating the morphology To further investigate the behavior of particle descriptors of
 and texture of particles, bivariate distributions of two- lunar regolith simulants, we parametrically model their uni-
 dimensional descriptor vectors should be considered. In variate and multivariate probability distributions. In a forth-
 addition, in some cases, more than two descriptors should coming study, the resulting model parameters will be used
 be considered simultaneously. For example, sphericity and for the calibration and validation of stochastic 3D models of
 mean gray value of CSM-LHT-1 particles are not strongly regolith simulant particles.
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
### Equation candidates
- `p0008_eq_070`: negative correlation between volume (or surface area) and correlated ( r s = 0 . 07), but their joint distribution shows
  - crop: `regolith_b379e8689263dc6d/assets/equations/page_0008_equation_070.png`

### Figure / graphic candidates
- `p0008_figure_000`: Fig. 5. Estimated probability densities of particle volume, surface area, sphericity and aspect ratio. Highland simulants are shown as dashed lines, mare 2 0
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0008_figure_000.png`

## Page 9

Matthias Weber et al. 9 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Fig. 6. Top: Estimated probability densities of particle-wise mean gray values. Only the overall distributions are shown as there is no visible difference
 between them and the distributions for particle interior or surface. Bottom: Estimated probability densities of the coefficients of variation for particle
 interior, surface, and overall. Highland simulants are shown as dashed lines, mare simulants as solid lines.
 
 Table 3. Mean Values of Particle Descriptors. 
 highland mare 
 CSM- LHS-1 OB1A JSC-1A LMS-1 OPRL2N CSM- 
 LHT-1 LMT-1 
 V [μm3] 57906 51287 50990 55298 92874 31634 60802 
 A [μm2] 6186 6235 7029 6846 9236 4900 6954 
 D [μm] 55.10 59.27 66.68 60.31 71.08 54.44 58.82 
 F 
 S 0.86 0.83 0.79 0.84 0.83 0.82 0.85 
 R 2.45 2.83 3.35 2.29 2.78 2.80 2.30 
 μ(G ) 11311 9966 15256 13691 11337 13313 13172 
 interior 
 μ(G ) 11380 10186 14209 13313 10917 12925 12991 
 surface 
 μ(G ) 11355 10135 14285 13398 10995 12965 13023 
 total 
 cv(G ) 0.07 0.06 0.06 0.08 0.07 0.07 0.08 
 interior 
 cv(G ) 0.08 0.07 0.08 0.10 0.09 0.09 0.09 
 surface 
 cv(G ) 0.08 0.07 0.08 0.10 0.09 0.09 0.09 
 total 
 Particle number 25660 24819 33751 23923 16413 45372 19566 
 As can be seen from Figures 5and 6, most univariate distri- It turned out that for the volume V and the sphericity S of
 butions of particle descriptors are not Gaussian, which implies CSM-LHT-1 particles the generalized inverse Gaussian distri-
 that more sophisticated tools (than multivariate Gaussian dis- bution and the normal inverse Gaussian distribution, respective-
 tributions) are needed in order to parametrically model the ly, provide the best fits, see Figure 9. The optimal parameter
 multivariate distributions of descriptor vectors. In the follow- values of these distributions are given in Table 4, which also con-
 ing, we exemplarily show how the copula-based approach ex- tains the best fitting parameter values of the Gaussian mixture
 plained earlier can be used to fit parametric bi- and trivariate model for the mean gray value μ(G) of CSM-LHT-1 particles.
 t 
 distributions to descriptor vectors consisting of volumes, In the next step, we apply the pair-copula approach stated in
 sphericities or/and mean gray values of CSM-LHT-1 particles. Section “R-Vine Copulas” to model the the joint probability
 In a first step, univariate parametric distributions are fitted to density f:R3 →[0,∞) of the three-dimensional random vec-
 the data for each of these particle descriptors, as visualized in tor (X ,X ,X )=(V,S,μ(G)). For this, according to the re-
 1 2 3 t 
 Figure 9, where the following procedure is used. For the volume presentation formula for f given in Equation (8), we need to
 V and sphericity S of CSM-LHT-1 particles, respectively, the best determine the bivariate copulas C , C and C (resp.
 1,3|2 1,2 2,3 
 fitting type of a unimodal probability density is chosen among their densities c , c and c ), which we chose from the
 1,3|2 1,2 2,3 
 those parametric families of distributions implemented in the sci- families of Gaussian, Clayton, Gumbel, Frank, Joe, BB1 and
 py package (Virtanen et al., 2020). Furthermore, for the mean BB8 copulas (Nelsen, 2006; Joe, 2014), using the pyvinecopu-
 gray value μ(G) of CSM-LHT-1 particles, a Gaussian mixture lib package (Vinecopulib, 2023).
 t 
 model is considered. Recall that formulas for the univariate dens- It turned out that the family of BB1 copulas provides the best
 ities of these three types of parametric probability distributions fit for C and C , whereas the family of BB8 copulas suits best
 1,2 2,3 
 have been stated in Section “Univariate Distributions.” for C . Note that both, BB1 and BB8, are Archimedean
 1,3|2 
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
### Equation candidates
- `p0009_eq_042`: the data for each of these particle descriptors, as visualized in tor ( X 1 , X 2 , X 3 ) = ( V , S , μ ( G t )). For this, according to the re-
  - crop: `regolith_b379e8689263dc6d/assets/equations/page_0009_equation_042.png`

### Figure / graphic candidates
- `p0009_figure_000`: No caption detected
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0009_figure_000.png`
- `p0009_figure_001`: No caption detected
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0009_figure_001.png`

## Page 10

10 Microscopy and Microanalysis, 2026, Vol. 32, No. 2
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Fig. 7. Spearman’s rank correlation coefficients, denoted by rs∈[−1,1], for pairs of particle descriptors of CSM-LHT-1.
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Fig. 8. Histograms of the joint distribution of sphericity S and mean gray value μ(Gt) (overall) for two different numbers (denoted by n) of CSM-LHT-1
 particles. Left: Particles with volume V<2600μm3, n=2762, rs=0.35. Right: All particles, n=24734, rs=0.07.
 
 copulas as introduced in the corresponding section. The optimal Comparison to Lunar Regolith
 parameter values of these copulas are given in Table 5. So far, the analysis showed significant differences between
 To validate the copula-based model given in Tables 4and 5, the considered regolith simulants with respect to various
 we draw 10,000 realizations from the fitted distribution of descriptors of shape and texture. To showcase differences
 (V,S,μ(G t )) and visually compare resulting (bivariate) histo- between regolith simulants and actual lunar regolith,
 grams to corresponding histograms of descriptor values com- we additionally consider recently published 3D data of
 puted from CT images. In particular, Figure 10 shows the lunar regolith from Apollo samples 10084 and 14163
 bivariate histograms of measured data (top row) and model (Chiaramonti & Garboczi, 2024) and from the Chang’e-5
 realizations (bottom row) for (V,S) in the left column, mission (Wu et al., 2025). Note that for this analysis, we only
 (S,μ(G)) in the middle column, and (S,μ(G)) conditional consider particles with a volume larger than 15000μm3 to
 t t 
 on V<2600μm3 in the right column. avoid artifacts from segmentation, see also (Wu et al., 2025).
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026

### Tables
**Fig. 7. Spearman ’ s rank correlation coefficients, denoted by r s ∈ [ − 1, 1], for pairs of particle descriptors of CSM-LHT-1. m / a**
|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |

**Fig. 7. Spearman ’ s rank correlation coefficients, denoted by r s ∈ [ − 1, 1], for pairs of particle descriptors of CSM-LHT-1. m / a**
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

### Equation candidates
- `p0010_eq_078`: ( S , μ ( G t )) in the middle column, and ( S , μ ( G t )) conditional consider particles with a volume larger than 15000 μ m 3 to
  - crop: `regolith_b379e8689263dc6d/assets/equations/page_0010_equation_078.png`
- `p0010_eq_079`: on V < 2600 μ m 3 in the right column. avoid artifacts from segmentation, see also (Wu et al., 2025).
  - crop: `regolith_b379e8689263dc6d/assets/equations/page_0010_equation_079.png`

### Figure / graphic candidates
- `p0010_figure_000`: Fig. 7. Spearman ’ s rank correlation coefficients, denoted by r s ∈ [ − 1, 1], for pairs of particle descriptors of CSM-LHT-1. m / a
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0010_figure_000.png`
- `p0010_figure_001`: Fig. 7. Spearman ’ s rank correlation coefficients, denoted by r s ∈ [ − 1, 1], for pairs of particle descriptors of CSM-LHT-1. m / a
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0010_figure_001.png`

## Page 11

Matthias Weber et al. 11 
 
 
 
 
 
 
 
 
 
 
 
 Fig. 9. Fitted parametric probability densities for the volume V (left), sphericity S (middle) and mean gray value μ(Gt) (right) of CSM-LHT-1 particles.
 
 Table 4. Types and Optimal Parameter Values of the Fitted Univariate explained by a dependence of particle shape on particle size.
 Distributions. E.g., smaller particles (by volume and surface area), which
 contribute to the first peaks of the corresponding distributions
 descriptor distribution parameters 
 could be less spherical, thereby exhibiting unexepectedly high
 V gen. inv. G. p=−0.99,b=0.070, values of aspect ratio and Feret diameter.
 l=−2059,s=315450 
 In general, highland simulants, shown as dashed lines in
 S norm. inv. G. a=2.47 
 l=0.91,s=0.11 Figure 5, seem to contain a larger fraction of fine particles
 μ(G 
 t 
 ) G. mixture p=0.38,μ 
 1 
 =13729,μ 
 2 
 =9879, with low volume and surface area than mare simulants (solid
 σ 1=1776,σ 2=792 lines). With respect to sphericity (and less so, aspect ratio),
 OB1A exhibits distinctly different particle shapes compared
 to all other simulants while the distributions of volume and
 surface area do not show this distinction. Particles of OB1A
 Table 5. Types and Optimal Parameter Values of the Fitted Bivariate tend to be less spherical with a higher aspect ratio which
 Copulas. may hint at more plate- or rod-shaped particles, which is in ac-
 descriptor pair copula type parameters rotation cordance with the visual impression from Figure 2.
 Considering the distributions of mean gray values and the
 V,S BB1 a=0.75,b=1.07 270◦ 
 coefficients of variation of gray values, huge differences be-
 S V , , μ μ ( ( G G t t ) )|S B B B B 8 1 a θ = = 0 1 . . 0 0 8 9 , , b δ= = 0 1 . . 9 0 4 1 2 1 7 8 0 0◦ ◦ tween the individual simulants can be observed, see
 Figure 6. Note that while the coefficient of variation is inde-
 pendent of the scale, the mean gray values (and individual vox-
 el gray values) lie between 0 and 65535, represented as 16-bit
 This roughly coincides with the lower limit of 25μm diameter integers. Note that the distribution of the coefficients of vari-
 present for the measured regolith simulants. Figure 11 shows ation for the gray values in the interior of OB1A particles is
 the distributions of particle volume for all considered samples. a kind of outlier, which is clearly bimodal and thus vastly dif-
 ferent from those of all other simulants. In all other cases, the
 Discussion distributions of mean gray values and coefficients of variations
 of gray values do not differ considerably between particle sur-
 In this section we discuss the methods and results presented in 
 face and interior. Thus, in the following, we will not make this
 this paper. In particular, the next section discusses the results 
 distinction and instead consider the overall gray value
 of the univariate analysis, followed by a section on the multi- 
 distributions. 
 variate analysis and model fits. Finally, we discuss the implica- 
 With the exception of OB1A, as mentioned above, no clear
 tions of our findings in terms of comparability between 
 differences can be seen in Figure 6between the distributions of
 different regolith simulants and lunar regolith. 
 the coefficients of variation for the individual simulants.
 However, the distributions of mean gray values show pro-
 Univariate Data Analysis nounced similarities and differences. For most simulants, ex-
 In the following, we discuss the univariate distributions of cept LMS-1, the probability densities of mean gray values
 morphological and textural descriptors. Keep in mind that, have peaks at either roughly 9000 or 13000, or both. This
 as shown in Table 1, the constituents of regolith simulants dif- may hint at two main groups of constituents across all
 fer widely. Moreover, the simulants are produced using differ- simulants. 
 ent methods. Therefore, we expect different simulants to Quantitatively, the heights of these peaks differ significantly
 exhibit variations in the descriptor distributions. between simulants, as shown in the top row of Figure 6. For
 Notably, the rough shapes of the probability densities of example, most mare simulants, namely JSC-1A, OPRL2N
 volume, surface area, sphericity, Feret diameter and aspect ra- and CSM-LMT-1, exhibit their major peak at roughly
 tio shown in Figures 5are similar for most simulants, where 13000. In addition, JSC-1A and OPRL2N show a minor
 bimodal distributions can be observed for volume and surface peak at 9000. In contrast, the highland simulants LHS-1,
 area for all simulants except for LHS-1 and LMS-1. None of CSM-LHT-1 and OB1A have their major peak at roughly
 the simulants exhibit bimodal distributions for sphericity, 9000, with CSM-LHT-1 and OB1A exhibiting a secondary
 Feret diameter and aspect ratio. The apparent inconsistencies peak at roughly 13000 and 24000, respectively. On the other
 between bimodal and unimodal distributions may be hand, LMS-1 shows an entirely different behavior with two
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
### Figure / graphic candidates
- `p0011_figure_000`: Fig. 9. Fitted parametric probability densities for the volume V (left), sphericity S (middle) and mean gray value μ ( G t ) (right) of CSM-LHT-1 particles.
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0011_figure_000.png`
- `p0011_figure_001`: Fig. 9. Fitted parametric probability densities for the volume V (left), sphericity S (middle) and mean gray value μ ( G t ) (right) of CSM-LHT-1 particles.
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0011_figure_001.png`

## Page 12

12 Microscopy and Microanalysis, 2026, Vol. 32, No. 2
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Fig. 10. Bivariate histograms of measured data (top row) and simulated data drawn from the fitted copula-based model (bottom row), for CSM-LHT-1
 particles. Left: Volume V vs. sphericity S. Middle: Sphericity S vs. mean gray value μ(Gt). Right: Sphericity S vs. mean gray value μ(Gt) given that
 V<2600μm3, see also the histograms shown in Figure 8. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Fig. 11. Comparison of estimated probability densities of particle volumes for lunar regolith (Apollo samples 10084, 14163 and Chang’e-5) and regolith
 simulants. Left: Mare samples. Right: Highlands samples. 
 
 peaks at around 8500 and 10800 where no peaks are located wise probability densities are located. Similarly, the peaks of
 for the other simulants. the particle-wise probability densities of CSM-LHT-1 and
 Although the mean values given in Table 3cannot fully cap- LHS-1 are reflected in their global mean values. Notably,
 ture the information of the mostly bimodal distributions of the OB1A shows the highest mean gray value, heavily influenced
 various particle descriptors, the main differences observed in by the secondary peak at 24000, visualized in the top row of
 Figures 5 and 6 are reflected in the mean values of Table 3. Figure 6. Regarding descriptors of particle shape, the mean
 In particular, JSC-1A, OPRL2N and CSM-LMT-1 show (glo- values of Table 3roughly correspond to the visual impression
 bal) mean gray values near 13000, i.e., roughly at the same of Figure 5. Notably, the mean values given in Table 3for vol-
 place where the major peaks of the corresponding particle- ume and surface area show that the tails of the corresponding
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
### Figure / graphic candidates
- `p0012_figure_000`: No caption detected
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0012_figure_000.png`
- `p0012_figure_001`: Fig. 11. Comparison of estimated probability densities of particle volumes for lunar regolith (Apollo samples 10084, 14163 and Chang ’ e-5) and regolith
  - crop: `regolith_b379e8689263dc6d/assets/figures/page_0012_figure_001.png`

## Page 13

Matthias Weber et al. 13 
 
 particle-wise distributions are comparatively heavy, leading to simulants and lunar regolith. Moreover, the distribution differs
 mean values significantly higher than the visually perceived between lunar regolith from different landing sites, even for two
 peaks of the distributions. mare landing sites from Apollo sample 10084 and the Chang’e
 mission. Bearing in mind that the lunar regolith samples have
 been measured and analyzed using different techniques, it is un-
 Multivariate Data Analysis and Parametric 
 clear to what extent these measured differences correspond to
 Modeling 
 actual differences in material. These uncertainties together
 In this section, we discuss the results of the multivariate ana- 
 with the huge differences between regolith simulants and lunar
 lysis and parametric modeling performed for CSM-LHT-1 
 regolith corroborate the need for further investigations of actual
 particles, as presented in Sections 3.2 and 3.3. Figure 7indi- 
 lunar regolith and the development of a digital twin for regolith
 cates that particle volume and surface area are strongly corre- 
 from different landing sites. 
 lated, both negatively with sphericity, while aspect ratio 
 For future comparisons of lunar regolith samples and rego-
 exhibits no clear correlation with size-related descriptors, sug- 
 lith simulants, the performed parametric modeling can be em-
 gesting elongated particles occur across all sizes. Considering 
 ployed as an efficient and systematic framework to quantify
 correlations between size and texture of particles, the coeffi- 
 and compare the morphology and texture of different samples.
 cients of variation of particle-wise gray values are strongly 
 In particular, this reduces complex 3D image data, of irregular-
 positively correlated to particle sizes, i.e., volumes and surface 
 ly shaped particles, to relatively few interpretable parameters
 areas of particles. This might indicate that larger particles are 
 that characterize the multivariate probability distribution of de-
 more likely to be composed of a mixture of different materials, 
 scriptor vectors. Therefore, the comparison of different regolith
 which can also be observed in Figure 2. While further analysis 
 samples can be reduced to a quantitative comparison of inter-
 of this behavior lies beyond the scope of the present paper, this 
 pretable parameters. 
 could be reconsidered in a forthcoming study when trying to 
 Beyond characterization, the inferred multivariate distribu-
 stochastically model the inner structure of particles. The fact 
 tions can be deployed for computer-based predictions of how
 that two or even more particle descriptors can be correlated 
 different types of regolith behave as feed materials during pro-
 is supported by the (conditional) bivariate histograms visual- 
 cessing operations. As demonstrated in related work on particle
 ized in Figure 8, further, supporting the need of multivariately 
 processing (Furat et al., 2020), the multivariate distribution of
 characterizing regolith particles, as performed in the section 
 descriptor vectors influence bulk behavior and processing per-
 on parametric modeling. 
 formance, further strengthening the case for digital, data-driven
 In particular, in that section, multivariate probability densities 
 modeling approaches. 
 have been fitted to descriptor vectors by initially fitting paramet- 
 ric univariate marginal distributions, see Figure 9, followed by 
 the deployment of parametric copulas to achieve bivariate fits, Conclusion and Outlook
 see Figure 10. As can be seen from Figure 10, the histograms of 
 In-Situ Resource Utilization (ISRU) plays a crucial role for future
 measured data (top row) are quite similar to the corresponding 
 space exploration activities. A key aspect of ISRU is the produc-
 histograms of data simulated by the fitted copula-based model 
 tion of oxygen from locally available resources such as, e.g., the
 (bottom row), i.e., the copula-based model given in Tables 4 
 lunar regolith when planning long-term human presence on the
 and 5is indeed capable of capturing the empirical distributions 
 moon. All approaches for utilizing lunar regolith, including
 of particle descriptor vectors computed from CT image data. 
 the extraction of oxygen, require reliable mechanical handling
 of regolith. Compared to terrestrial applications, the lunar envir-
 Regolith Simulant Comparability and Digital onment and special properties of lunar regolith pose extraordin-
 Modeling ary challenges when developing parts for regolith handling.
 As outlined in the introduction, understanding the mechanical Thus, a profound understanding of the rheology of lunar rego-
 properties of lunar regolith—especially under the conditions lith is required for fast and reliable development of regolith
 of reduced gravity and vacuum—is essential for enabling reli- handling equipment.
 able regolith handling and processing during future lunar mis- In the present paper, we took a first step towards a better
 sions. Since experimental studies conducted under terrestrial understanding of mechanical properties of lunar regolith by
 conditions often use regolith simulants as substitutes for lunar outlining the methodology needed for understanding key as-
 regolith, it is equally interesting to understand how regolith sim- pects of regolith by CT imaging and subsequent statistical ana-
 ulants behave mechanically. However, the univariate analysis lysis of certain morphological and textural particle descriptors.
 performed in this work indicates that regolith simulants that Using this approach, we analyzed seven samples of different
 try to replicate the same type of lunar regolith (mare, highlands) regolith simulants with respect to their size, shape and texture.
 differ significantly in terms of morphology and texture. Although the various simulants exhibit some similarities,
 However, since morphology and composition of particles also we found significant differences with respect to particle-wise
 affect their mechanical properties, it is unclear to what extent texture (gray values) and, for some simulants, also with re-
 the mechanical properties of the simulants under consideration spect to particle shape, see Table 3. As it has been shown for
 are comparable to those of lunar regolith. While a detailed com- other particulate materials that the (morphological and tex-
 parison with the lunar regolith considered in the present paper is tural) descriptors of particles correlate with their behavior in
 difficult because the sample preparation, imaging and image mechanical processing, we may expect similar correlations
 processing steps used to collect the open source data of lunar for regolith simulants. In a forthcoming study, we plan to in-
 regolith (Chiaramonti & Garboczi, 2024; Goguen et al., vestigate these relationships in order to be able to predict the
 2024; Wu et al., 2025) do not necessarily correspond to the steps unknown behavior of lunar regolith under lunar conditions.
 described in this paper, a basic comparison of particle size distri- For these future investigations, we plan to measure the rhe-
 bution already shows huge differences between regolith ology of the same regolith simulants under near-lunar
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
## Page 14

14 Microscopy and Microanalysis, 2026, Vol. 32, No. 2
 
 conditions in a parabolic flight facility. The methods and basic Baidya S, Melius M, Hassan AM, Sharits A, Chiaramonti AN, Lafarge
 analyses established in the present paper will lay the founda- T, Goguen JD & Garboczi EJ(2022). Optical scattering characteris-
 tion for correlating the behavior of regolith simulants in vari- tics of 3–D lunar regolith particles measured using X–ray nano com-
 ous experiments with their microstructure. puted tomography. IEEE Geosci Remote Sens Lett 19, 1–5. https://
 In addition to a descriptive statistical analysis of size, shape doi.org/10.1109/LGRS.2021.3073344
 Barndorff-Nielsen O, Blæsild P & Halgreen C(1978). First hitting time
 and texture of regolith simulant particles, we performed a 
 models for the generalized inverse gaussian distribution. Stoch
 multivariate analysis of particle descriptor vectors and para- 
 Process Appl 7(1), 49–54. https://doi.org/10.1016/0304-4149(78)
 metrically modeled the joint distribution of three descriptors 
 90036-4 
 of size, shape and texture, using a copula-based modeling ap- 
 Berg S, Kutra D, Kroeger T, Straehle CN, Kausler BX, Haubold C,
 proach. This analysis and the capability to parametrically re- 
 Schiegg M, Ales J, Beier T, Rudy M, Eren K, Cervantes JI, Xu B,
 present the joint distribution of an arbitrary number of Beuttenmueller F, Wolny A, Zhang C, Koethe U, Hamprecht FA
 particle descriptors may serve as a basis for the development & Kreshuk A(2019). ilastik: Interactive machine learning for (bio)-
 of a stochastic 3D model for regolith particles. image analysis. Nat Methods 16(12), 1226–1232. ISSN 1548–7105.
 In a forthcoming study, we will develop such a model to en- https://doi.org/10.1038/s41592-019-0582-9
 able the in-silico analysis of different scenarios for better Birch T, Seidel A, Monchieri E, Franz M, Weber M, Schmidt V, Furat O,
 understanding how various aspects of regolith, specifications Peuker U, Ditscherlein R, Ditscherlein L, Schilde C, Lamping T,
 of regolith handling equipment and its effective behavior Pöhle G & Redlich C(2025). UPREB: Universal predictors of rego-
 lith behaviour – concept and overview. In Proceedings of the 54th
 and performance are linked with each other. Then, in addition 
 International Conference on Environmental Systems, Prague, to the development of a stochastic 3D model for regolith par-
 Lapensee S & Abney M (Eds.), ICES-2025-109.
 ticles, this approach of virtual materials testing will also re- 
 Buzug TM(2008). Computed Tomography: From Photon Statistics to
 quire some work on the calibration of numerical models for 
 Modern Cone–Beam CT. Berlin, Heidelberg: Springer.
 the particle behavior in mechanical processing to experimental 
 Chiaramonti A & Garboczi E(2024). 3D shape and size data for 10084
 data obtained from experiments performed under near-lunar and 14163 lunar regolith particles. National Institute of Standards
 conditions. and Technology. Accessed: 2024-11-04. https://doi.org/10.18434/
 mds2-3043 
 Availability of Data and Materials Czado C(2019). Analyzing Dependent Data with Vine Copulas. Cham:
 Springer. 
 The authors have declared that no datasets apply for this Deng J, Qian Y, Cui F, Liu Y & Lai J(2025). Research on lunar regolith
 piece. of the Chang’e-4 landing site: An automated analysis method based
 on deep learning framework. Icarus 425, 116338. ISSN 0019–1035.
 Acknowledgments https://doi.org/10.1016/j.icarus.2024.116338
 Ditscherlein R, Leißner T & Peuker UA(2022). Preparation strategy for
 We thank Rostislav Kovtun (NASA Johnson Space Center) for statistically significant micrometer–sized particle systems suitable
 providing the samples, Annett Kästner for assistance in sample for correlative 3D imaging workflows on the example of X–ray mi-
 preparation, and Thomas Buchwald for guidance on particle- crotomography. Powder Technol 395, 235–242. https://doi.org/10.
 discrete extraction. 1016/j.powtec.2021.09.038 
 Englisch S, Ditscherlein R, Kirstein T, Hansen L, Furat O, Drobek D,
 Leißner T, Zubiri BA, Weber AP, Schmidt V, Peuker UA &
 Author Contributions Statement 
 Spiecker E(2023). 3D analysis of equally X-ray attenuating mineral-
 M.W., M.F., U.A.P., A.S., V.S., and G.P. conceived the ana- ogical phases utilizing a correlative tomographic workflow across
 lysis, R.D. and L.D. measured the tomographic image data multiple length scales. Powder Technol 419(2–3), 118343. ISSN
 of regolith simulants, M.W. and R.D. analyzed the data. 0032–5910. https://doi.org/10.1016/j.powtec.2023.118343
 M.W., R.D., T.B., A.S., O.F., and V.S. wrote and reviewed Erdoğan ST, Garboczi ET & Fowler DW(2007). Shape and size of mi-
 the manuscript. crofine aggregates: X–ray microcomputed tomography vs. laser dif-
 fraction. Powder Technol 177(2), 53–63. https://doi.org/10.1016/j.
 powtec.2007.02.016 
 Financial Support 
 Furat O, Kirstein T, Leißner T, Bachmann K, Gutzmer J, Peuker UA &
 This work was funded by the Federal Ministry for Economic Schmidt V (2024). Multidimensional characterization of particle
 Affairs and Energy (BMWE), based on a resolution of the morphology and mineralogical composition using CT data and
 German Parliament (grant number 50EX2367A-B). R-vine copulas. Miner Eng 206(3), 108520. ISSN 0892–6875.
 https://doi.org/10.1016/j.mineng.2023.108520
 Furat O, Masuhr M, Kruis FE & Schmidt V(2020). Stochastic modeling
 Conflict of Interest 
 of classifying aerodynamic lenses for separation of airborne particles
 No competing interests are declared. by material and size. Adv. Powder Technol 31(6), 2215–2226. ISSN
 0921–8831. https://doi.org/10.1016/j.apt.2020.03.014
 Goguen J, Sharits A, Chiaramonti A, Lafarge T & Garboczi E(2024).
 Three-dimensional characterization of particle size, shape, and in-
 References 
 ternal porosity for Apollo 11 and Apollo 14 lunar regolith and
 Aigner K-M, Schaumann P, von Loeper F, Martin A, Schmidt V & Liers JSC-1A lunar regolith soil simulant. Icarus 420(1974), 116166.
 F(2023). Robust DC optimal power flow with modeling of solar ISSN 0019–1035. https://doi.org/10.1016/j.icarus.2024.116166
 power supply uncertainty via R-vine copulas. Optim Eng 24(3), Haeming M, Seidel A & Zell U(2020). Electrolysis apparatus for the
 1951–1982. https://doi.org/10.1007/s11081-022-09761-0 electrolytic production of oxygen from oxide-containing starting
 Azami M, Kazemi Z, Moazen S, Dubé M, Potvin M-J & Skonieczny K material. US11479869B2, 2020-10-12.
 (2024). A comprehensive review of lunar-based manufacturing and Haff IH, Aas K & Frigessi A(2010). On the simplified pair-copula con-
 construction. Prog Aerosp Sci 150(4), 101045. ISSN 0376–0421. struction–simply useful or too simplistic. J Multivar Anal 101(5),
 https://doi.org/10.1016/j.paerosci.2024.101045 1296–1310. https://doi.org/10.1016/j.jmva.2009.12.001
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
## Page 15

Matthias Weber et al. 15 
 
 Isachenkov M, Chugunov S, Landsman Z, Akhatov I, Metke A, Geometry for Computer Imagery, Kuba A, Nyúl L & Palágyi K
 Tikhonov A & Shishkovsky I(2022). Characterization of novel lunar (Eds.), pp. 247–258. Berlin, Heidelberg: Springer.
 highland and mare simulants for ISRU research applications. Icarus Schulz B, Sandmann D & Gilbricht S (2020). SEM-based automated
 376(1), 114873. https://doi.org/10.1016/j.icarus.2021.114873 mineralogy and its application in geo- and material sciences.
 Joe H (2014). Dependence Modeling with Copulas. Bosa Roca: Minerals 10(11), 1004. https://doi.org/10.3390/min10111004
 Chapman and Hall/CRC. Schulze D(2021). Powders and Bulk Solids. Cham: Springer.
 Jung A, Redenbach C, Schladitz K & Staub S(2022). 3D image-based Seidel A, Altenburg M, Monchieri E, Strigl F, Quadbeck P, Redlich C &
 stochastic micro-structure modelling of foams for simulating elasti- Pal U(2022). ROXY – An economically viable process to produce
 city. In Research in Mathematics of Materials Science, pp. 257–281. oxygen and metals from regolith. In Proceedings of the 51st
 Cham: Springer. International Conference on Environmental Systems, Saint Paul,
 Kafka OL, Moser NH, Chiaramonti AN, Garboczi EJ, Wilkerson RP & MN, Leimkuehler T & Macleod S (Eds.), ICES-2022-140.
 Rickman DL(2025). Measurement of the three-dimensional shape Seidel A, Monchieri E, Kübler U, Pal U, Pöhle G, Redlich C, Charitos A,
 and size distribution of 17 lunar regolith simulants: Simulant shape Vogt D, Driebe T & Grellmann R(2023). Mini-ROXY: The next
 and size inter-comparison and simulant shape comparison with step towards an efficient method for oxygen extraction from regoli-
 Apollo 11 and Apollo 14 lunar regolith. Icarus 434(14–15), thy. Annual Meeting of the American Society for Gravitational and
 116542. ISSN 0019–1035. https://doi.org/10.1016/j.icarus.2025. Space Research.
 116542 Seidel A, Pal UB, Quadbeck P & Adrian A(2021). Method and system
 Katagiri J, Matsushima T, Yamada Y, Tsuchiyama A, Nakano T, Uesugi for extracting metal and oxygen from powdered metal oxides.
 K, Ohtake M & Saiki K(2015). Investigation of 3D grain shape char- US20230131891A1, 2021-10-25.
 acteristics of lunar soil retrieved in Apollo 16 using image-based Sibille L, Carpenter P, Schlagheck R & French RA(2006). Lunar rego-
 discrete-element modeling. J Aerosp Eng 28(4), 04014092. ISSN lith simulant materials: Recommendations for standardization, pro-
 1943–5525. https://doi.org/10.1061/(ASCE)AS.1943-5525.0000421 duction, and usage. Technical Report NASA/TP—2006–214605.
 Laurini KC & Gerstenmaier WH(2014). The global exploration road- https://ntrs.nasa.gov/api/citations/20060051776/downloads/2006
 map and its significance for NASA. Space Policy 30(3), 149–155. 0051776.pdf. Accessed: 2024-09-12.
 https://doi.org/10.1016/j.spacepol.2014.08.004 Sittner J, Da Assuncao Godinho JR, Renno A, Cnudde V, Boone M,
 Li L, Hui H, Hu S, Li Q, Chen Y, Yang W, Tang G, Jia L, Li X, Gu L & Schryver Td, van Loo D, Merkulova M, Roine A & Liipo J
 Wu F (2025). Discovery of carbonaceous chondritic fragment in (2020). Spectral X-ray computed micro tomography: 3-dimensional
 Chang’e-5 regolith samples. Icarus 429(2094), 116454. ISSN chemical imaging. X-Ray Spectrom 50(2), 92–105. https://doi.org/
 0019–1035. https://doi.org/10.1016/j.icarus.2025.116454 10.1002/xrs.v50.2 
 Li R, Zhou G, Yan K, Chen J, Chen D, Cai S & Mo P-Q (2022). Spettl A, Dosta M, Bachstein S, Heinrich S & Schmidt V (2016).
 Preparation and characterization of a specialized lunar regolith Microstructural effects in breakage behavior of real and virtual ag-
 simulant for use in lunar low gravity simulation. Int J Min Sci glomerates under compressive load: Automated extraction of intern-
 Technol 32(1), 1–15. ISSN 2095–2686. https://doi.org/10.1016/j. al microstructures, their stochastic modeling and copula-based
 ijmst.2021.09.003 breakage models fitted to DEM data. In Proceedings of the
 Lin CL & Miller JD(2005). 3D characterization and analysis of particle International Congress on Particle Technology, Nürnberg.
 shape using X–ray microtomography (XMT). Powder Technol Paper-ID 1.18. 
 154(1), 61–69. https://doi.org/10.1016/j.powtec.2005.04.031 Tsuchiyama A, Sakurama T, Nakano T, Uesugi K, Ohtake M,
 Martin A & Wagoner C(2022). JHU-APL LSII REPORT: 2022 Lunar Matsushima T, Terakado K & Galimov EM (2022).
 Simulant Assessment. Technical report, Johns Hopkins Applied Three-dimensional shape distribution of lunar regolith particles
 Physics Laboratory. https://lsic.jhuapl.edu/Our-Work/Working- collected by the Apollo and Luna programs. Earth Planets Space
 Groups/files/Lunar-Simulants/2022%20Lunar%20Simulants%20 74(1), 172. ISSN 1880–5981. https://doi.org/10.1186/s40623-022-
 Assessment%20Final.pdf. Accessed: 2024-12-09. 01737-9 
 Nelsen RB (2006). An Introduction to Copulas. New York, NY: Tsuchiyama A, Yamaguchi H, Ogawa M, Nakamura AM, Michikami T
 Springer. & Uesugi K(2025). Abrasion experiments of mineral, rock, and me-
 Neumann M, Furat O, Hlushkou D, Tallarek U, Holzer L & Schmidt V teorite particles: Simulating regolith particles abrasion on airless
 (2018). On microstructure-property relationships derived by virtual bodies. Icarus 429(6486), 116432. ISSN 0019–1035. https://doi.
 materials testing with an emphasis on effective conductivity. In org/10.1016/j.icarus.2024.116432
 Simulation Science, Baum M, Brenner G, Grabowski Jens, Tute RM & Goulas A(2024). Mechanical behaviour of sulphur-based
 Hanschke T, Hartmann Stefan & Schöbel A (Eds.), pp. 145–158, martian regolith concrete processed under CO 2 -rich conditions.
 Cham: Springer International Publishing. Icarus 417, 116134. ISSN 0019–1035. https://doi.org/10.1016/j.
 Otto H, Kerst K, Roloff C, Janiga G & Katterfeld A(2018). CFD-DEM icarus.2024.116134
 simulation and experimental investigation of the flow behavior of lu- Van der Walt S, Schönberger JL, Nunez-Iglesias J, Boulogne F, Warner
 nar regolith JSC-1A. Particuology 40(1), 34–43. ISSN 1674–2001. JD, Yager N, Gouillart E & Yu T(2014). scikit-image: Image pro-
 https://doi.org/10.1016/j.partic.2017.12.003 cessing in python. PeerJ 2(2), e453. https://doi.org/10.7717/peerj.
 Peng B, Hay R & Celik K(2023). 3D shape analysis of lunar regolith 453 
 simulants. Powder Technol 426(3), 118621. ISSN 0032–5910. Vinecopulib(2023). Vinecopulib/pyvinecopulib: A python library for
 https://doi.org/10.1016/j.powtec.2023.118621 vine copula models. https://github.com/vinecopulib/pyvinecopulib.
 Pourakbar M, Zhao Y, Cortes DD & Dai S(2025). Small-strain thermo- Accessed: 2023-04-20.
 mechanical performance of lunar mare and highlands regolith simu- Virtanen P, Gommers R, Oliphant TE, Haberland M, Reddy T,
 lants under Earth’s atmospheric pressure and in vacuum. Icarus Cournapeau D, Burovski E, Peterson P, Weckesser W, Bright J,
 429(3–4), 116405. ISSN 0019–1035. https://doi.org/10.1016/j. van der Walt SJ, Brett M, Wilson J, Jarrod Millman K, Mayorov
 icarus.2024.116405 N, Nelson ARJ, Jones E, Kern R, Larson E, Carey CJ, Polat İ,
 Prifling B, Westhoff D, Schmidt D, Markoetter H, Manke I, Knoblauch Feng Y, Moore EW, VanderPlas J, Laxalde D, Perktold J,
 V & Schmidt V(2019). Parametric microstructure modeling of com- Cimrman R, Henriksen I, Quintero EA, Harris CR, Archibald
 pressed cathode materials for li-ion batteries. Comput Mater Sci AM, Ribeiro AH, Pedregosa F & van Mulbregt P, SciPy 1.0
 169(8), 109083. https://doi.org/10.1016/j.commatsci.2019.109083 Contributors(2020). SciPy 1.0: Fundamental algorithms for scien-
 Schladitz K, Ohser J & Nagel W(2007). Measuring intrinsic volumes in tific computing in python. Nat Methods 17(3), 261–272. https://
 digital 3D images. In 13th International Conference on Discrete doi.org/10.1038/s41592-019-0686-2
 Downloaded
 from
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 by 
 guest
 on 
 24 
 April
 2026
## Page 16

16 Microscopy and Microanalysis, 2026, Vol. 32, No. 2
 
 Weber M, Grießer A, Glatt E, Wiegmann A & Schmidt V (2022). computed tomography. Nat Rev Methods Primers 1(1), 18. https://
 Modeling curved fibers by fitting R-vine copulas to their frenet rep- doi.org/10.1038/s43586-021-00015-4
 resentations. Microsc Microanal 29(1), 155–165. ISSN 1431–9276. Wu H, Zou Y, Zhang C, Yang W, Wu B, Yung K-L & Zhao Q(2025).
 https://doi.org/10.1093/micmic/ozac030 Micro-CT characterization of the Chang’e-5 Lunar regolith samples.
 Weber M, Grießer A, Mosbach D, Glatt E, Wiegmann A & Schmidt V 
 J Geophys Res Planets 130(3), e2024JE008787. https://doi.org/10.
 (2024). Investigating microstructure–property relationships of non- 
 1029/2024JE008787 
 wovens by model-based virtual material testing. Transp Porous 
 Zanon P, Dunn M & Brooks G(2024). Lunar simulant behaviour vari-
 Media 151(6), 1403–1421. https://doi.org/10.1007/s11242-024- 
 02079-8 ability and implications on terrestrial based lunar testing. Icarus
 Withers PJ, Bouman C, Carmignato S, Cnudde V, Grimaldi D, Hagen 422(1), 116257. ISSN 0019-1035. https://doi.org/10.1016/j.icarus.
 CK, Maire E, Manley M, Plessis Ad & Stock SR (2021). X–ray 2024.116257 
 Downloaded
 from
 
 https://academic.oup.com/mam/article/32/2/ozag013/8519522
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 by 
 guest
 on 
 24 
 April
 2026
