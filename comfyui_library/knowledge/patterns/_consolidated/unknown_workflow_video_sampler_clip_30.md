---
name: unknown_workflow_video_sampler_clip_30
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.7906
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, GetNode, JWInteger, KSamplerAdvanced, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, RIFE VFI, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, wanBlockSwap]
problems: []
missing: []
members: [图片生成/文生图/文生视频+高动态++Smooth+Mix+Wan2.2_2051825137523142657.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V 图生视频最强动态搭配_1982410881613078529.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980829288985444354.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配（lora版）_1982062028078620674.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V高动态首尾帧_1980947136646959105.json, 视频生成/图生视频/Wan2.2 Remix V2图生视频版_1986648481861431297.json, 视频生成/图生视频/Wan2.2 Smooth Mix图生视频（高动态）_1979541039348355074.json, 视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_1979545928719831042.json, 视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_2017190232734568450.json, 视频生成/图生视频/Wan2.2-DaSiWa-最强动漫模型-首尾帧视频-插帧放大-自动提示词_2010927245770100738.json, 视频生成/图生视频/Wan2.2动漫模型DaSiWa-首尾帧视频_2013598944579821569.json, 视频生成/图生视频/Wan2.2动漫模型DaSiWa-首尾帧视频_2076910094813589506.json, 视频生成/图生视频/动漫短剧图生视频动态优化工作流（lora版+自动提示词）_1982328615742382081.json, 视频生成/图生视频/图生视频 Wan2.2 Remix 高画质高动态_1987454672774565889.json, 视频生成/图生视频/（lora版）WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980995649351061505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/文生视频+高动态++Smooth+Mix+Wan2.2_2051825137523142657.json、视频生成/图生视频/WAN2.2-LightX2V-I2V 图生视频最强动态搭配_1982410881613078529.json、视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980829288985444354.json、视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配（lora版）_1982062028078620674.json、视频生成/图生视频/WAN2.2-LightX2V-I2V高动态首尾帧_1980947136646959105.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `GetNode`
- `JWInteger`
- `KSamplerAdvanced`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `RIFE VFI`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 14/15 个有
- `CLIPVisionLoader` —— 14/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/15 个有
- `LoadImage` —— 14/15 个有
- `easy showAnything` —— 14/15 个有
- `Fast Groups Bypasser (rgthree)` —— 13/15 个有
- `ImpactSwitch` —— 13/15 个有
- `ImageConcanate` —— 9/15 个有
- `WanImageToVideo` —— 9/15 个有
- `LoraLoaderModelOnly` —— 8/15 个有
- `Text Concatenate` —— 8/15 个有
- `Wan22PromptSelector` —— 8/15 个有
- `ImageResizeKJ` —— 6/15 个有
- `ShowText|pysssss` —— 6/15 个有
- `WanFirstLastFrameToVideo` —— 6/15 个有
- `Text Multiline` —— 3/15 个有
- `LayerUtility: PurgeVRAM V2` —— 2/15 个有
- `VHS_LoadVideo` —— 2/15 个有
- `AddLabel` —— 1/15 个有
- `CR Text Input Switch (4 way)` —— 1/15 个有
- `ImageStitch` —— 1/15 个有
- `PDIMAGE_LongerSize` —— 1/15 个有
- `RunningHub Deepcleaner` —— 1/15 个有
- `easy textSwitch` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 15 | 53% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 15 | 92% |
| 采样算法 | 1 | 1 - 1 | 15 | 100% |
| 调度器 | euler_ancestral | - | 15 | 80% |
| 重绘幅度 | simple | - | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，15 个样本，一致性 53%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，15 个样本，取值集中（一致性 92%）
- 采样算法 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，15 个样本，一致性 80%
- 重绘幅度 最常用 simple，15 个样本，一致性 100%
