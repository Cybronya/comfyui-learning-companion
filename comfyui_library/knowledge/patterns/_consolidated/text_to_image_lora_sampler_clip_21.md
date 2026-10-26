---
name: text_to_image_lora_sampler_clip_21
type: Text To Image
frequency: 25
level: strong
coverage: 0.88116
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/RH Upscale双版本视频放大，极速高清视频超分处理_2110500573517795329.json, 图片生成/图生图/RH Upscale双版本视频超分，极速高清放大处理_2110877348689170433.json, 图片生成/图生图/RH Upscale视频极速超分｜RH币版加api版双通道_2111134972022185985.json, 图片生成/图生图/SeedVR2zip批量放大｜多图一次导入批量超分出图_2106570411403206657.json, 图片生成/图生图/SeedVR2人像写真专用｜顶级画质高清放大不糊脸_2106568757719166978.json, 图片生成/图生图/SeedVR2材质细节增强｜图生图高清放大保留纹理_2106567237770502146.json, 图片生成/图生图/SeedVR2材质细节放大｜图生图修复纹理质感_2097231310170447874.json, 图片生成/图生图/Vosr2.0+RTX视频串联修复｜超高清画质增强工作流_2097831528368791553.json, 图片生成/图生图/zip多图打包批量处理｜SeedVR2图片高清放大流水线_2106559487606878210.json, 图片生成/图生图/全能图片G image 2.0图生图官方稳定版｜修图稳如老狗_2111833584133828610.json, 图片生成/图生图/全能图片G-2图生图 官方稳定版Image 2商品摄影_2098692462993829889.json, 图片生成/图生图/全能图片G2.0官方稳定版 图生图可靠直出方案_2110371560384192514.json, 图片生成/图生图/全能图片G2.0官方稳定版 图生图质量有保障_2104656322951208962.json, 图片生成/图生图/全能图片G2.0官方稳定版图生图处理生成工具_2101741663516450817.json, 图片生成/图生图/全能图片G2.0官方稳定版工作流，图生图多场景覆盖处理工具_2105762042266349569.json, 图片生成/图生图/全能图片G2.0官方稳定版，图生图多任务一个流程搞定_2112650204284542978.json, 图片生成/图生图/全能图片G2.0官方稳定版｜图生图一键直出_2089281828489355265.json, 图片生成/图生图/全能图片G2.0官方稳定版｜图生图全能编辑_2090083955017080833.json, 图片生成/图生图/全能图片G2.0官方稳定版｜图生图多场景通用的放心之选_2101572295738355714.json, 图片生成/图生图/全能图片G2.0官方稳定版｜图生图老牌优选｜稳定输出不翻车_2102582375585763330.json, 图片生成/图生图/官方稳定版全能图片｜G2.0图生图处理直出_2092759621646766081.json, 图片生成/图生图/批量图片高清放大zip多图加SeedVR2，电商主图详情页印刷素材批量高清_2106816793737256962.json, 数字人/数字人/RH Upscale双版本RH币API版视频极速高清放大，视频超分工具_2105803495495524354.json, 数字人/数字人/视频高清RH Upscale双模式工作流，数字人视频生视频超分处理工具_2106869306951819265.json, 视频生成/图生视频/视频高清RH_Upscale双模式工作流，数字人视频生视频超分处理工具_2109815199111925761.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/RH Upscale双版本视频放大，极速高清视频超分处理_2110500573517795329.json、图片生成/图生图/RH Upscale双版本视频超分，极速高清放大处理_2110877348689170433.json、图片生成/图生图/RH Upscale视频极速超分｜RH币版加api版双通道_2111134972022185985.json、图片生成/图生图/SeedVR2zip批量放大｜多图一次导入批量超分出图_2106570411403206657.json、图片生成/图生图/SeedVR2人像写真专用｜顶级画质高清放大不糊脸_2106568757719166978.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 25 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 24/25 个有
- `SaveImage` —— 21/25 个有
- `LoadImage` —— 16/25 个有
- `RH_RhartImageG2OfficialImageToImage` —— 12/25 个有
- `LoadVideo` —— 6/25 个有
- `RH_RhartVideoVideoUpscaler` —— 6/25 个有
- `RH_Upscale` —— 6/25 个有
- `SeedVR2` —— 6/25 个有
- `SaveVideo` —— 5/25 个有
- `RHUploadZip_V2` —— 3/25 个有
- `Fast Groups Bypasser (rgthree)` —— 2/25 个有
- `GetVideoComponents` —— 2/25 个有
- `VHS_VideoCombine` —— 2/25 个有
- `EmptyImage` —— 1/25 个有
- `PreviewAny` —— 1/25 个有
- `PreviewImage` —— 1/25 个有
- `RH_BytedanceSeedance25TokenImageToVideo` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 25 | 100% |
| 采样算法 | er_sde | - | 25 | 100% |
| 调度器 | beta | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 80 | 80 - 80 | 25 | 100% |
| 高度 | 80 | 80 - 80 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 26/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，25 个样本，一致性 100%
- 调度器 最常用 beta，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高发问题（26/25 个样本）：Steps较低可能导致细节不足
