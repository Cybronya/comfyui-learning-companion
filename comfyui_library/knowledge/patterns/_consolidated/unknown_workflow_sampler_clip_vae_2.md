---
name: unknown_workflow_sampler_clip_vae_2
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.984
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, SaveVideo, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1988041568177295362.json, 视频生成/图生视频/1988138088604004353.json, 视频生成/图生视频/1982368438184230913.json, 视频生成/图生视频/2044955303057301505.json, 视频生成/图生视频/2049008127445573634.json, 视频生成/图生视频/2079750552161968129.json, 视频生成/图生视频/2077588507496894466.json, 视频生成/图生视频/2079019127112556545.json, 视频生成/图生视频/2079108169829273601.json, 视频生成/图生视频/2082362157714460674.json, 视频生成/图生视频/2082287620427706369.json, 视频生成/图生视频/2064561200037457922.json, 视频生成/图生视频/1950521447607357441.json, 视频生成/图生视频/1956163238578847745.json, 视频生成/图生视频/1950557926740119553.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_2

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/1988041568177295362.json、视频生成/图生视频/1988138088604004353.json、视频生成/图生视频/1982368438184230913.json、视频生成/图生视频/2044955303057301505.json、视频生成/图生视频/2049008127445573634.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `SaveVideo`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/15 个有
- `ModelSamplingSD3` —— 14/15 个有
- `UNETLoader` —— 14/15 个有
- `WanImageToVideo` —— 14/15 个有
- `PathchSageAttentionKJ` —— 12/15 个有
- `CFGZeroStar` —— 10/15 个有
- `SimpleMath+` —— 3/15 个有
- `ImpactInt` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `Text` —— 2/15 个有
- `Int` —— 1/15 个有
- `TrimVideoLatent` —— 1/15 个有
- `UnetLoaderGGUF` —— 1/15 个有
- `WanVaceToVideo` —— 1/15 个有
- `workflow>LORA1` —— 1/15 个有
- `workflow>LORA2` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 15 | 93% |
| Prompt 约束强度(CFG) | 20 | 4 - 20 | 15 | 63% |
| 采样算法 | 3.5 | 1 - 3.5 | 15 | 61% |
| 调度器 | euler | - | 15 | 100% |
| 重绘幅度 | simple | - | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，15 个样本，一致性 93%
- Prompt 约束强度(CFG) 中位数 20，观测区间 4 - 20，15 个样本
- 采样算法 中位数 3.5，观测区间 1 - 3.5，15 个样本
- 调度器 最常用 euler，15 个样本，一致性 100%
- 重绘幅度 最常用 simple，15 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
