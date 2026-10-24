---
name: unknown_workflow_video_lora_sampler_22
type: Unknown Workflow
frequency: 28
level: strong
coverage: 0.985857
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, CheckpointLoaderSimple, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/live动图-图生视频_起号神器_wan2.2_2092082949134053377.json, 视频生成/图生视频/Wan2.2  彩图解码版_1992982649104957441.json, 视频生成/图生视频/Wan2.2 极速 All-in-one｜图生视频_2089372780319035394.json, 视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2071113609022885889.json, 视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2071129553375944706.json, 视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2071500994327965698.json, 视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2072199531965542401.json, 视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2073056519012306946.json, 视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2073072648741015553.json, 视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2075260707406442498.json, 视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2079226151834316802.json, 视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2079972635341058049.json, 视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2093357480247119873.json, 视频生成/图生视频/Wan2.2+All-in-one+极速版+图生视频_2089535977193820162.json, 视频生成/图生视频/Wan2.2+All-in-one图生视频极速版_2019656477216088065.json, 视频生成/图生视频/live动图-图生视频_起号神器_wan2.2_2038320886633209857.json, 视频生成/图生视频/人物表情真实自然+Wan2.2_2039989765587607554.json, 视频生成/图生视频/图生视频-Wan2.2-极速版_2069950709994442753.json, 视频生成/图生视频/图生视频Wan2.2+All-in-one_2044586130233888770.json, 视频生成/图生视频/图生视频Wan2.2+All-in-one急速稳定专用版本_2042866151662821378.json, 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_1983515933761314818.json, 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_2041324315588698113.json, 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_2069791627677356033.json, 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_2099699527749038082.json, 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_2099791658589188097.json, 视频生成/图生视频/图生视频Wan2.2_2046033851276857346.json, 视频生成/图生视频/图生视频Wan2.2_空挡braless_2062575894211948546.json, 视频生成/图生视频/图生视频Wan2.2稳定专用版本_2044590119671304193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/文生图/live动图-图生视频_起号神器_wan2.2_2092082949134053377.json、视频生成/图生视频/Wan2.2  彩图解码版_1992982649104957441.json、视频生成/图生视频/Wan2.2 极速 All-in-one｜图生视频_2089372780319035394.json、视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2071113609022885889.json、视频生成/图生视频/Wan2.2+All-in-one 极速版 图生视频_2071129553375944706.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 28 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `JWFloat` —— 27/28 个有
- `MathExpression|pysssss` —— 27/28 个有
- `LoadLatent` —— 13/28 个有
- `VAELoader` —— 13/28 个有
- `SaveImage` —— 11/28 个有
- `Int` —— 2/28 个有
- `TT_img_enc_v2` —— 2/28 个有
- `TwoWaySwitch` —— 2/28 个有
- `DuckHideNode` —— 1/28 个有
- `PrimitiveBoolean` —— 1/28 个有
- `ZML_SwitchOutput` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 28 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 28 | 100% |
| 采样算法 | sa_solver | - | 28 | 100% |
| 调度器 | beta | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，28 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，28 个样本，一致性 100%
- 调度器 最常用 beta，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 高发问题（28/28 个样本）：Steps较低可能导致细节不足
