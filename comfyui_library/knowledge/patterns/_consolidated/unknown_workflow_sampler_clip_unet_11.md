---
name: unknown_workflow_sampler_clip_unet_11
type: Unknown Workflow
frequency: 15
level: weak
coverage: 0.9394
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1952176106529083393.json, 视频生成/图生视频/1983855179189620738.json, 视频生成/图生视频/1950086411632467970.json, 视频生成/图生视频/1951916750197698561.json, 视频生成/图生视频/Wan3.0图生视频_2093297268513394689.json, 视频生成/图生视频/1949982981533384705.json, 视频生成/图生视频/1949988822005235714.json, 视频生成/图生视频/1950054777926369282.json, 视频生成/图生视频/1950460812701949953.json, 视频生成/图生视频/1950007304294981633.json, 视频生成/图生视频/1954724255986544642.json, 视频生成/图生视频/1949851914386194434.json, 视频生成/图生视频/1950015498596564993.json, 视频生成/图生视频/1950053385758269442.json, 视频生成/图生视频/1954125145533247489.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/1952176106529083393.json、视频生成/图生视频/1983855179189620738.json、视频生成/图生视频/1950086411632467970.json、视频生成/图生视频/1951916750197698561.json、视频生成/图生视频/Wan3.0图生视频_2093297268513394689.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `WanImageToVideo` —— 12/15 个有
- `MathExpression|pysssss` —— 9/15 个有
- `ImageResizeKJv2` —— 8/15 个有
- `PathchSageAttentionKJ` —— 8/15 个有
- `Primitive integer [Crystools]` —— 8/15 个有
- `Text Multiline` —— 8/15 个有
- `LoraLoaderModelOnly` —— 7/15 个有
- `WanFirstLastFrameToVideo` —— 3/15 个有
- `Label (rgthree)` —— 2/15 个有
- `Int` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 15 | 67% |
| Prompt 约束强度(CFG) | 20 | 4 - 20 | 15 | 47% |
| 采样算法 | 3.5 | 1 - 4 | 15 | 44% |
| 调度器 | euler | - | 15 | 60% |
| 重绘幅度 | simple | - | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，15 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 20，观测区间 4 - 20，15 个样本，取值分散，一致性仅 47%
- 采样算法 中位数 3.5，观测区间 1 - 4，15 个样本，取值分散，一致性仅 44%
- 调度器 最常用 euler，15 个样本，一致性 60%
- 重绘幅度 最常用 simple，15 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
