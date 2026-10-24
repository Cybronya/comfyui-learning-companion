---
name: text_to_image_lora_sampler_clip_87
type: Text To Image
frequency: 15
level: strong
coverage: 0.895867
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/首尾帧图文一键生视频｜MiniMax H3加速版数字人_2095958370124656641.json, 视频生成/图生视频/首尾帧生视频！加速版MiniMaxH3转场特效数字人图生视频_2085455030794145794.json, 视频生成/文生视频/H3全能参考生视频MiniMax视频生视频图生视频_2086209628857266177.json, 视频生成/文生视频/MiniMax H3图生视频加速版｜首尾帧衔接流畅运镜_2107650568532619266.json, 视频生成/文生视频/MiniMax H3图生视频首尾帧加速版 高效视频生成工具_2098651353672404993.json, 视频生成/文生视频/MiniMax H3图生视频首尾帧加速版｜文生视频图生视频 过渡更丝滑_2104044437436456962.json, 视频生成/文生视频/MiniMax H3图生视频首尾帧视频加速版 高质量动态生成_2105359652836962306.json, 视频生成/文生视频/MiniMax H3图生视频首尾帧视频加速版工作流，文生视频图生视频处理方案_2108271446815494146.json, 视频生成/文生视频/MiniMax H3图生视频首尾帧视频加速版，文生视频图生视频高效方案_2106824742857691137.json, 视频生成/文生视频/MiniMax H3首尾帧视频加速版｜图生视频快速过运镜_2108027039709229058.json, 视频生成/文生视频/MiniMax H3首尾帧视频加速版｜图生视频高效出片方案_2105118748511399938.json, 视频生成/文生视频/加速版MiniMax H3图生视频首尾帧视频工作流，文生视频视频运镜图生视频_2107890229058297858.json, 视频生成/文生视频/加速版首尾帧视频生成｜MiniMax H3图生视频运镜控制_2097043511534243841.json, 视频生成/文生视频/首尾帧精准控制 MiniMax H3图生视频加速版流畅出片_2104266521487958017.json, 视频生成/文生视频/首尾帧视频加速版｜MiniMax H3图生视频生成_2094749515961163777.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_87

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/首尾帧图文一键生视频｜MiniMax H3加速版数字人_2095958370124656641.json、视频生成/图生视频/首尾帧生视频！加速版MiniMaxH3转场特效数字人图生视频_2085455030794145794.json、视频生成/文生视频/H3全能参考生视频MiniMax视频生视频图生视频_2086209628857266177.json、视频生成/文生视频/MiniMax H3图生视频加速版｜首尾帧衔接流畅运镜_2107650568532619266.json、视频生成/文生视频/MiniMax H3图生视频首尾帧加速版 高效视频生成工具_2098651353672404993.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 14/15 个有
- `EasyCache` —— 14/15 个有
- `MiniMaxH3ImageToVideo` —— 14/15 个有
- `PathchSageAttentionKJ` —— 14/15 个有
- `孤海注释` —— 14/15 个有
- `ImageResizeKJv2` —— 13/15 个有
- `ShowAnything|Mie` —— 13/15 个有
- `CM_IntToFloat` —— 12/15 个有
- `Int` —— 12/15 个有
- `SaveImage` —— 7/15 个有
- `GetNode` —— 3/15 个有
- `PrimitiveFloat` —— 3/15 个有
- `ResolutionSelector` —— 3/15 个有
- `SetNode` —— 3/15 个有
- `AILab_QwenVL_Advanced` —— 1/15 个有
- `DF_Int_to_Float` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `Image Stitch` —— 1/15 个有
- `ImageScaleDownToSize` —— 1/15 个有
- `LayerUtility: PurgeVRAM` —— 1/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/15 个有
- `MiniMaxH3ReferenceToVideo` —— 1/15 个有
- `easy imageScaleDownToSize` —— 1/15 个有
- `easy positive` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
