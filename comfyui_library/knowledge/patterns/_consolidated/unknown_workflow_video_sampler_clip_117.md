---
name: unknown_workflow_video_sampler_clip_117
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.764167
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2官方版图生视频_1992405756192550914.json, 视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频+智能扩写提示词_1979084209711124482.json, 视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频--智能扩写提示词版_1978821829475340289.json, 视频生成/图生视频/【官版】Wan2.2-Lightning4步加速图生视频_1955176719431843842.json, 视频生成/图生视频/高动态-图生视频-WAN2.2-LightX2V-I2V_1981728832514334722.json, 视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979825054756278274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_117

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/wan2.2官方版图生视频_1992405756192550914.json、视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频+智能扩写提示词_1979084209711124482.json、视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频--智能扩写提示词版_1978821829475340289.json、视频生成/图生视频/【官版】Wan2.2-Lightning4步加速图生视频_1955176719431843842.json、视频生成/图生视频/高动态-图生视频-WAN2.2-LightX2V-I2V_1981728832514334722.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 5/6 个有
- `CLIPVisionLoader` —— 5/6 个有
- `ImpactSwitch` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `wanBlockSwap` —— 5/6 个有
- `Text Concatenate` —— 4/6 个有
- `Wan22PromptSelector` —— 4/6 个有
- `PrimitiveInt` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `RIFE VFI` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `ImpactInt` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `ModelPatchTorchSettings` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `GetImageSizeAndCount` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 67% |
| Prompt 约束强度(CFG) | 5 | 4 - 6 | 6 | 80% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler_ancestral | - | 6 | 50% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 6，6 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，6 个样本，一致性 50%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
