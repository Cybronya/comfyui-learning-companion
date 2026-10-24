---
name: unknown_workflow_video_lora_sampler_730
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.954
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CR Prompt Text, Int, JWStringConcat, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveInt, RHHiddenNodes, RH_Captioner, RH_LLMAPI_NODE, SimpleMath+, TextConcat, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, Wan22PromptSelector, WanImageToVideo, easy anythingIndexSwitch, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/AI短剧角色表演万相2.2 ​高动态官方图生视频_1961337086731337730.json, 视频生成/图生视频/官方万相wan2.2图生视频极速版+自动扩写_1953068357463511042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_730

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/AI短剧角色表演万相2.2 ​高动态官方图生视频_1961337086731337730.json、视频生成/图生视频/官方万相wan2.2图生视频极速版+自动扩写_1953068357463511042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `Int`
- `JWStringConcat`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RHHiddenNodes`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `SimpleMath+`
- `TextConcat`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanImageToVideo`
- `easy anythingIndexSwitch`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 14 | - | 2 | 100% |
| 采样算法 | 2.25 | - | 2 | 44% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 14，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
