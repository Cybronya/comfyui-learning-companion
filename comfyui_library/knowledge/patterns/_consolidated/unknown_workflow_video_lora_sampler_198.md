---
name: unknown_workflow_video_lora_sampler_198
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8072
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1992405756192550914.json, 视频生成/图生视频/1979084209711124482.json, 视频生成/图生视频/1978821829475340289.json, 视频生成/图生视频/1955176719431843842.json, 视频生成/图生视频/1982328615742382081.json, 视频生成/图生视频/1987454672774565889.json, 视频生成/图生视频/1981008328186806273.json, 视频生成/图生视频/1981728832514334722.json, 视频生成/图生视频/1981000332023042050.json, 视频生成/图生视频/1980995649351061505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_198

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1992405756192550914.json、视频生成/图生视频/1979084209711124482.json、视频生成/图生视频/1978821829475340289.json、视频生成/图生视频/1955176719431843842.json、视频生成/图生视频/1982328615742382081.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 9/10 个有
- `wanBlockSwap` —— 9/10 个有
- `easy showAnything` —— 8/10 个有
- `CR Text` —— 7/10 个有
- `JWInteger` —— 7/10 个有
- `RIFE VFI` —— 7/10 个有
- `GetNode` —— 6/10 个有
- `ImpactSwitch` —— 6/10 个有
- `ModelPatchTorchSettings` —— 6/10 个有
- `SetNode` —— 6/10 个有
- `ShowText|pysssss` —— 6/10 个有
- `Fast Groups Bypasser (rgthree)` —— 5/10 个有
- `SeedVR2BlockSwap` —— 5/10 个有
- `SeedVR2ExtraArgs` —— 5/10 个有
- `SeedVR2GGUF` —— 5/10 个有
- `Text Concatenate` —— 5/10 个有
- `Wan22PromptSelector` —— 5/10 个有
- `CR Text Input Switch` —— 2/10 个有
- `ImpactInt` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `GetImageSizeAndCount` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `easy textSwitch` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 60% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 10 | 83% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler_ancestral | - | 10 | 70% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，10 个样本，取值集中（一致性 83%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，10 个样本，一致性 70%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
