---
name: text_to_image_video_lora_sampler_120
type: Text To Image
frequency: 6
level: strong
coverage: 0.728167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimax首尾帧视频加速生成｜图生视频快速出片工作流_2097079966373601282.json, 视频生成/图生视频/单图生视频 MiniMax H3 图片驱动角色表演_2094228080427622401.json, 视频生成/图生视频/单图生视频版本｜MiniMax+H3角色设计表演生成_2094589153349554177.json, 视频生成/文生视频/人物角色文生视频｜MiniMax+H3角色设计一键生成_2094312279473999874.json, 视频生成/文生视频/开源文生视频｜MiniMax-H3战斗特效角色设计生成_2094797659730169857.json, 视频生成/文生视频/文生视频 MiniMax H3 可设时长分辨率比例快速出片_2094174814998192130.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_120

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/minimax首尾帧视频加速生成｜图生视频快速出片工作流_2097079966373601282.json、视频生成/图生视频/单图生视频 MiniMax H3 图片驱动角色表演_2094228080427622401.json、视频生成/图生视频/单图生视频版本｜MiniMax+H3角色设计表演生成_2094589153349554177.json、视频生成/文生视频/人物角色文生视频｜MiniMax+H3角色设计一键生成_2094312279473999874.json、视频生成/文生视频/开源文生视频｜MiniMax-H3战斗特效角色设计生成_2094797659730169857.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `VHS_LoadVideoFFmpeg` —— 5/6 个有
- `LoadImage` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `Text` —— 3/6 个有
- `ImageCrop+` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `Any Switch (rgthree)` —— 1/6 个有
- `DF_Int_to_Float` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `H3SigmaRefiner` —— 1/6 个有
- `Int` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `SolAttnPatch` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
