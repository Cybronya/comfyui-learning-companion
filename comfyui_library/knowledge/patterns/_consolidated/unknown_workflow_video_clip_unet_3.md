---
name: unknown_workflow_video_clip_unet_3
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.951882
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImpactInt, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, Seed (rgthree), SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2035302183196954625.json, 视频生成/图生视频/2003315240559312897.json, 视频生成/图生视频/1989316468380717058.json, 视频生成/图生视频/1982107238137511938.json, 视频生成/图生视频/1981536473277177858.json, 视频生成/图生视频/2011239621144875009.json, 视频生成/图生视频/1981294713347145729.json, 视频生成/图生视频/2079544662850887682.json, 视频生成/图生视频/Wan2.2-Smooth Mix飞行少女飞行滑板多图首尾帧图生视频 超丝滑首尾帧工作流_2087859368317505538.json, 视频生成/图生视频/2001506323961397250.json, 视频生成/图生视频/2013454725135470593.json, 视频生成/图生视频/2055911477286064130.json, 视频生成/图生视频/2017823753580847106.json, 视频生成/图生视频/飞行少女飞行滑板多图首尾帧首尾帧图生视频Wan2.2-Smooth Mix 超丝滑首尾帧工作流_2011515988684050433.json, 视频生成/图生视频/飞行少女飞行滑板多图首尾帧首尾帧图生视频Wan2.2-Smooth Mix 超丝滑首尾帧工作流_2103812745828327426.json, 视频生成/图生视频/2005234314344361986.json, 视频生成/图生视频/1988422481260232705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/2035302183196954625.json、视频生成/图生视频/2003315240559312897.json、视频生成/图生视频/1989316468380717058.json、视频生成/图生视频/1982107238137511938.json、视频生成/图生视频/1981536473277177858.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImpactInt`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Seed (rgthree)`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 16/17 个有
- `ImageResizeKJv2` —— 16/17 个有
- `ImageScaleBy` —— 16/17 个有
- `Mute / Bypass Repeater (rgthree)` —— 16/17 个有
- `RIFE VFI` —— 16/17 个有
- `easy cleanGpuUsed` —— 16/17 个有
- `KSamplerAdvanced` —— 15/17 个有
- `PrimitiveStringMultiline` —— 15/17 个有
- `WanFirstLastFrameToVideo` —— 11/17 个有
- `ImageBatchExtendWithOverlap` —— 7/17 个有
- `WanAdvancedI2V` —— 7/17 个有
- `WanImageToVideo` —— 4/17 个有
- `CR Text` —— 2/17 个有
- `PainterI2V` —— 2/17 个有
- `Text Concatenate` —— 2/17 个有
- `WanMoeKSampler` —— 2/17 个有
- `easy float` —— 2/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/17 个有
- `Note Plus (mtb)` —— 1/17 个有
- `RH_LLMAPI_NODE` —— 1/17 个有
- `RH_Translator` —— 1/17 个有
- `Wan22PromptSelector` —— 1/17 个有
- `easy showAnything` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 17 | 59% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 17 | 100% |
| 采样算法 | 1 | 1 - 1 | 17 | 100% |
| 调度器 | euler_ancestral | - | 17 | 82% |
| 重绘幅度 | simple | - | 17 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，17 个样本，一致性 59%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，17 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，17 个样本，一致性 82%
- 重绘幅度 最常用 simple，17 个样本，一致性 82%
