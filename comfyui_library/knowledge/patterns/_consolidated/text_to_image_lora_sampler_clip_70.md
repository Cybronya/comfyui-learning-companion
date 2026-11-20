---
name: text_to_image_lora_sampler_clip_70
type: Text To Image
frequency: 17
level: strong
coverage: 0.896353
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/RH Upscale双版本视频放大，极速高清视频超分处理_2110500573517795329.json, 图片生成/图生图/RH Upscale双版本视频超分，极速高清放大处理_2110877348689170433.json, 图片生成/图生图/RH Upscale视频极速超分｜RH币版加api版双通道_2111134972022185985.json, 图片生成/图生图/SeedVR2zip批量放大｜多图一次导入批量超分出图_2106570411403206657.json, 图片生成/图生图/SeedVR2人像写真专用｜顶级画质高清放大不糊脸_2106568757719166978.json, 图片生成/图生图/SeedVR2材质细节增强｜图生图高清放大保留纹理_2106567237770502146.json, 图片生成/图生图/SeedVR2材质细节放大｜图生图修复纹理质感_2097231310170447874.json, 图片生成/图生图/Vosr2.0+RTX视频串联修复｜超高清画质增强工作流_2097831528368791553.json, 图片生成/图生图/zip多图打包批量处理｜SeedVR2图片高清放大流水线_2106559487606878210.json, 图片生成/图生图/全能图片G image 2.0图生图官方稳定版｜修图稳如老狗_2111833584133828610.json, 图片生成/图生图/官方稳定版全能图片｜G2.0图生图处理直出_2092759621646766081.json, 图片生成/图生图/批量图片高清放大zip多图加SeedVR2，电商主图详情页印刷素材批量高清_2106816793737256962.json, 数字人/数字人/DLSS5视频图片超分辨率 Video Image Super Resolution增强_2098709137747169282.json, 视频生成/文生视频/RH Upscale视频极速高清放大工作流PR插件适配，视频超分高清增强工具_2107260285441634305.json, 视频生成/文生视频/RH Upscale视频极速高清放大工作流，PR插件适配视频超分工具_2106535133057740802.json, 视频生成/文生视频/Seedance 2.5图生视频处理生成工具_2102525837089263617.json, 视频生成/文生视频/Seedance2.0 Fast全能参考视频 图片音频视频三参考输入_2104694435845070849.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/RH Upscale双版本视频放大，极速高清视频超分处理_2110500573517795329.json、图片生成/图生图/RH Upscale双版本视频超分，极速高清放大处理_2110877348689170433.json、图片生成/图生图/RH Upscale视频极速超分｜RH币版加api版双通道_2111134972022185985.json、图片生成/图生图/SeedVR2zip批量放大｜多图一次导入批量超分出图_2106570411403206657.json、图片生成/图生图/SeedVR2人像写真专用｜顶级画质高清放大不糊脸_2106568757719166978.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 12/17 个有
- `LoadImage` —— 9/17 个有
- `SaveVideo` —— 9/17 个有
- `LoadVideo` —— 7/17 个有
- `SeedVR2` —— 6/17 个有
- `RH_Upscale` —— 5/17 个有
- `RHUploadZip_V2` —— 3/17 个有
- `RH_RhartVideoVideoUpscaler` —— 3/17 个有
- `RH_BytedanceSeedance25TokenImageToVideo` —— 2/17 个有
- `RH_RhartImageG2OfficialImageToImage` —— 2/17 个有
- `Image Comparer (rgthree)` —— 1/17 个有
- `LoadAudio` —— 1/17 个有
- `RH_DLSS5Enhance` —— 1/17 个有
- `RH_RhartVideoSparkvideo20FastMultimodalVideo` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（19/17 个样本）：Steps较低可能导致细节不足
