---
name: unknown_workflow_video_sampler_clip_78
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.618125
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Smooth Mix Wan 2.2：首尾帧驱动！_1999138314991042561.json, 视频生成/图生视频/Wan2.2 Smooth高质量图生视频极速版_2033413176150204417.json, "视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V一镜到底,超强动态，高质量，高遵循度API_2006247037502758914.json", 视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_1999107369680371713.json, 视频生成/图生视频/video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2000487723846729730.json, 视频生成/图生视频/video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2006292810990882817.json, 视频生成/图生视频/图生视频 _ 高动态 _ wan smooth_1988988553113776129.json, 视频生成/图生视频/图生视频自动切镜头WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2003771509095211009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_78

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Smooth Mix Wan 2.2：首尾帧驱动！_1999138314991042561.json、视频生成/图生视频/Wan2.2 Smooth高质量图生视频极速版_2033413176150204417.json、视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V一镜到底,超强动态，高质量，高遵循度API_2006247037502758914.json、视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_1999107369680371713.json、视频生成/图生视频/video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2000487723846729730.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/8 个有
- `WanImageToVideo` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `easy int` —— 6/8 个有
- `wanBlockSwap` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `INTConstant` —— 5/8 个有
- `Int` —— 5/8 个有
- `CLIPVisionEncode` —— 3/8 个有
- `CLIPVisionLoader` —— 3/8 个有
- `JWInteger` —— 3/8 个有
- `Seed (rgthree)` —— 3/8 个有
- `WanFirstLastFrameToVideo` —— 3/8 个有
- `CR Prompt Text` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 62% |
| Prompt 约束强度(CFG) | 4 | 4 - 10 | 8 | 56% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 62% |
| 重绘幅度 | normal | - | 8 | 62% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 10，8 个样本
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 62%
- 重绘幅度 最常用 normal，8 个样本，一致性 62%
