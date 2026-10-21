---
name: unknown_workflow_sampler_clip_vae_6
type: Unknown Workflow
frequency: 13
level: weak
coverage: 0.950538
common_nodes: [CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SaveVideo, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1951683752307142657.json, 视频生成/图生视频/1950086411632467970.json, 视频生成/图生视频/1951916750197698561.json, 视频生成/图生视频/Wan3.0图生视频_2093297268513394689.json, 视频生成/图生视频/1949982981533384705.json, 视频生成/图生视频/1949988822005235714.json, 视频生成/图生视频/1950054777926369282.json, 视频生成/图生视频/1950460812701949953.json, 视频生成/图生视频/1950007304294981633.json, 视频生成/图生视频/1954724255986544642.json, 视频生成/图生视频/1949851914386194434.json, 视频生成/图生视频/1950015498596564993.json, 视频生成/图生视频/1973739180855529474.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_6

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1951683752307142657.json、视频生成/图生视频/1950086411632467970.json、视频生成/图生视频/1951916750197698561.json、视频生成/图生视频/Wan3.0图生视频_2093297268513394689.json、视频生成/图生视频/1949982981533384705.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 12/13 个有
- `UNETLoader` —— 12/13 个有
- `WanImageToVideo` —— 11/13 个有
- `ImageResizeKJv2` —— 9/13 个有
- `MathExpression|pysssss` —— 8/13 个有
- `Primitive integer [Crystools]` —— 8/13 个有
- `Text Multiline` —— 8/13 个有
- `PathchSageAttentionKJ` —— 7/13 个有
- `LoraLoaderModelOnly` —— 6/13 个有
- `WanFirstLastFrameToVideo` —— 2/13 个有
- `CLIPLoaderGGUF` —— 1/13 个有
- `LG_LoadImage` —— 1/13 个有
- `UnetLoaderGGUF` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 13 | 77% |
| Prompt 约束强度(CFG) | 20 | 4 - 20 | 13 | 46% |
| 采样算法 | 3.5 | 1 - 4 | 13 | 45% |
| 调度器 | euler | - | 13 | 62% |
| 重绘幅度 | simple | - | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，13 个样本，一致性 77%
- Prompt 约束强度(CFG) 中位数 20，观测区间 4 - 20，13 个样本，取值分散，一致性仅 46%
- 采样算法 中位数 3.5，观测区间 1 - 4，13 个样本，取值分散，一致性仅 45%
- 调度器 最常用 euler，13 个样本，一致性 62%
- 重绘幅度 最常用 simple，13 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
