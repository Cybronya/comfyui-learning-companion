---
name: unknown_workflow_video_lora_sampler_685
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.89825
common_nodes: [CLIPLoader, CLIPTextEncode, ImageToMask, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, MaskToImage, ModelSamplingSD3, PathchSageAttentionKJ, RepeatImageBatch, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo]
problems: []
missing: []
members: [平台全量/Wan2.2视频扩图实验版V1_1950024427478147073.json, 视频生成/图生视频/Wan2.2 Vace首尾帧_1950473543098290177.json, 视频生成/图生视频/Wan2.2 Vace首尾帧女孩变动漫_1950544723431903234.json, 视频生成/图生视频/Wan2.2 Vace首尾帧实验版V1_1950053355886436353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_685

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Wan2.2视频扩图实验版V1_1950024427478147073.json、视频生成/图生视频/Wan2.2 Vace首尾帧_1950473543098290177.json、视频生成/图生视频/Wan2.2 Vace首尾帧女孩变动漫_1950544723431903234.json、视频生成/图生视频/Wan2.2 Vace首尾帧实验版V1_1950053355886436353.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageToMask`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RepeatImageBatch`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 3/4 个有
- `ImageFromBatch+` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `SolidMask` —— 3/4 个有
- `GetVideoComponents` —— 1/4 个有
- `ImagePadForOutpaint` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 10 | 8 - 10 | 4 | 91% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | lcm | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 10，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
