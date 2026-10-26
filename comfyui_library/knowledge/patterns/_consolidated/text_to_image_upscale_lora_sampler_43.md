---
name: text_to_image_upscale_lora_sampler_43
type: Text To Image
frequency: 6
level: strong
coverage: 0.901167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/VOSR 高清修复放大｜图片视频通吃 文字破损也能强力修复_2097498871793541121.json, 图片生成/图生图/VOSR 高清放大修复｜图生图画质提升 文字强力修复不糊_2097519616615604226.json, 图片生成/图生图/VOSR2.0+DLLS5视频放大工作流｜Minimax-H3专用视频超分_2097405321030488065.json, 图片生成/图生图/VOSR2.0图片放大 高清图生图超分处理生成工具_2113739207758929922.json, 图片生成/图生图/VOSR2视频逐帧放大｜低显存友好文字不乱码_2105275285280223234.json, 图片生成/图生图/Vosr 2视频超分放大｜高清画质文字不乱码保障_2105279647989723137.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/VOSR 高清修复放大｜图片视频通吃 文字破损也能强力修复_2097498871793541121.json、图片生成/图生图/VOSR 高清放大修复｜图生图画质提升 文字强力修复不糊_2097519616615604226.json、图片生成/图生图/VOSR2.0+DLLS5视频放大工作流｜Minimax-H3专用视频超分_2097405321030488065.json、图片生成/图生图/VOSR2.0图片放大 高清图生图超分处理生成工具_2113739207758929922.json、图片生成/图生图/VOSR2视频逐帧放大｜低显存友好文字不乱码_2105275285280223234.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `VHS_LoadVideo` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `SaveImage` —— 4/6 个有
- `VHS_VideoInfo` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `easy int` —— 3/6 个有
- `GH_AudioVideoMerger` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `RH_DLSS5Enhance` —— 1/6 个有
- `RebatchImages` —— 1/6 个有
- `VHS_Unbatch` —— 1/6 个有
- `easy float` —— 1/6 个有
- `easy imageSizeByLongerSide` —— 1/6 个有
- `int _O` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
