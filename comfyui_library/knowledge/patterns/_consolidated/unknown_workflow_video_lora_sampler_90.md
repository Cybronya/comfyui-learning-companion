---
name: unknown_workflow_video_lora_sampler_90
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.971062
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1962517255911288834.json, 视频生成/图生视频/Wan2.2 极速 All-in-one｜图生视频_2089372780319035394.json, 视频生成/图生视频/2071113609022885889.json, 视频生成/图生视频/2071129553375944706.json, 视频生成/图生视频/2071500994327965698.json, 视频生成/图生视频/2072199531965542401.json, 视频生成/图生视频/2073056519012306946.json, 视频生成/图生视频/2073072648741015553.json, 视频生成/图生视频/2075260707406442498.json, 视频生成/图生视频/2079226151834316802.json, 视频生成/图生视频/2079972635341058049.json, 视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2093357480247119873.json, 视频生成/图生视频/Wan2.2+All-in-one+极速版+图生视频_2089535977193820162.json, 视频生成/图生视频/2019656477216088065.json, 视频生成/图生视频/live动图-图生视频_wan2.2_2095005372602994689.json, 视频生成/图生视频/2038320886633209857.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_90

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/1962517255911288834.json、视频生成/图生视频/Wan2.2 极速 All-in-one｜图生视频_2089372780319035394.json、视频生成/图生视频/2071113609022885889.json、视频生成/图生视频/2071129553375944706.json、视频生成/图生视频/2071500994327965698.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 15/16 个有
- `JWFloat` —— 15/16 个有
- `JWInteger` —— 15/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/16 个有
- `MathExpression|pysssss` —— 15/16 个有
- `SaveImage` —— 3/16 个有
- `LoadLatent` —— 2/16 个有
- `VAELoader` —— 2/16 个有
- `ImageResizeKJv2` —— 1/16 个有
- `Int` —— 1/16 个有
- `JoinStrings` —— 1/16 个有
- `LayerUtility: PurgeVRAM` —— 1/16 个有
- `Qwen3_VQA` —— 1/16 个有
- `RH_Captioner` —— 1/16 个有
- `ShowText|pysssss` —— 1/16 个有
- `TextInput_` —— 1/16 个有
- `TwoWaySwitch` —— 1/16 个有
- `easy showAnything` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | sa_solver | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
