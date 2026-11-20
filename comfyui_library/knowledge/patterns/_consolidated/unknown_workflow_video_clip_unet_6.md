---
name: unknown_workflow_video_clip_unet_6
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.667
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Smooth Mix Wan 2.2：首尾帧驱动！_1999138314991042561.json, 视频生成/图生视频/Wan2.2_Smooth Mix I2V图生视频_2014967936171118594.json, 视频生成/图生视频/Wan2.2_Smooth-Mix-I2V-常规图生视频和首尾帧生视频_1998270569793617921.json, 视频生成/图生视频/painterI2V_Smooth-Mix-I2V-动态强度可调版_1991393474855677954.json, "视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V一镜到底,超强动态，高质量，高遵循度API_2006247037502758914.json", 视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_1999107369680371713.json, 视频生成/图生视频/video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2000487723846729730.json, 视频生成/图生视频/video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2006292810990882817.json, 视频生成/图生视频/图生视频 _ 高动态 _ wan smooth_1988988553113776129.json, 视频生成/图生视频/图生视频自动切镜头WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2003771509095211009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Smooth Mix Wan 2.2：首尾帧驱动！_1999138314991042561.json、视频生成/图生视频/Wan2.2_Smooth Mix I2V图生视频_2014967936171118594.json、视频生成/图生视频/Wan2.2_Smooth-Mix-I2V-常规图生视频和首尾帧生视频_1998270569793617921.json、视频生成/图生视频/painterI2V_Smooth-Mix-I2V-动态强度可调版_1991393474855677954.json、视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V一镜到底,超强动态，高质量，高遵循度API_2006247037502758914.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `wanBlockSwap` —— 9/10 个有
- `Fast Groups Bypasser (rgthree)` —— 8/10 个有
- `INTConstant` —— 8/10 个有
- `Int` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `WanImageToVideo` —— 8/10 个有
- `KSamplerAdvanced` —— 7/10 个有
- `ModelSamplingSD3` —— 7/10 个有
- `easy int` —— 7/10 个有
- `CLIPVisionEncode` —— 5/10 个有
- `CLIPVisionLoader` —— 5/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `WanFirstLastFrameToVideo` —— 4/10 个有
- `WanMoeKSampler` —— 3/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `JWInteger` —— 2/10 个有
- `RIFE VFI` —— 2/10 个有
- `Seed (rgthree)` —— 2/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PainterI2V` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 60% |
| Prompt 约束强度(CFG) | 5 | 4 - 10 | 10 | 61% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler | - | 10 | 50% |
| 重绘幅度 | normal | - | 10 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 10，10 个样本
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 50%
- 重绘幅度 最常用 normal，10 个样本，一致性 50%
