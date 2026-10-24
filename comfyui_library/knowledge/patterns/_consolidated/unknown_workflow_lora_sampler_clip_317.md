---
name: unknown_workflow_lora_sampler_clip_317
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.753
common_nodes: [BerniniConditioning, CLIPLoader, CLIPTextEncode, CreateVideo, GetVideoComponents, ImageFromBatch, KSamplerAdvanced, LoadVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveInt, SaveVideo, UNETLoader, VAEDecode, VAELoader, easy showAnything, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/文生视频/Bernini-R 参考视频条件编辑流程_2062503695899783170.json, 视频生成/文生视频/Bernini-R视频编辑V2V_2062503672382320641.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_317

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Bernini-R 参考视频条件编辑流程_2062503695899783170.json、视频生成/文生视频/Bernini-R视频编辑V2V_2062503672382320641.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `GetVideoComponents`
- `ImageFromBatch`
- `KSamplerAdvanced`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `BerniniPromptEnhancer` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `StringReplace` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 14 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 14，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
