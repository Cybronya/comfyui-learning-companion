---
name: text_to_image_lora_sampler_clip_24
type: Text To Image
frequency: 18
level: strong
coverage: 0.918444
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/首尾帧图文一键生视频｜MiniMax H3加速版数字人_2095958370124656641.json, 视频生成/图生视频/首尾帧生视频！加速版MiniMaxH3转场特效数字人图生视频_2085455030794145794.json, 视频生成/文生视频/5秒1080p仅8分钟｜MiniMax-H3图生视频全节点注释版_2093768843360563202.json, 视频生成/文生视频/5秒1080p只要8分钟｜MiniMax-H3图生视频全节点注释_2094005447392063489.json, 视频生成/文生视频/5秒1080p文生视频8分钟出片 MiniMax-H3 全节点注释_2094187651468455937.json, 视频生成/文生视频/MiniMax H3加速版首尾帧图生视频处理工具_2101022392209461249.json, 视频生成/文生视频/MiniMax H3图生视频加速版｜首尾帧衔接流畅运镜_2107650568532619266.json, 视频生成/文生视频/MiniMax H3图生视频首尾帧加速版 高效视频生成工具_2098651353672404993.json, 视频生成/文生视频/MiniMax H3图生视频首尾帧加速版｜文生视频图生视频 过渡更丝滑_2104044437436456962.json, 视频生成/文生视频/MiniMax H3图生视频首尾帧视频加速版 高质量动态生成_2105359652836962306.json, 视频生成/文生视频/MiniMax H3图生视频首尾帧视频加速版工作流，文生视频图生视频处理方案_2108271446815494146.json, 视频生成/文生视频/MiniMax H3图生视频首尾帧视频加速版，文生视频图生视频高效方案_2106824742857691137.json, 视频生成/文生视频/MiniMax H3首尾帧视频加速版｜图生视频快速过运镜_2108027039709229058.json, 视频生成/文生视频/MiniMax H3首尾帧视频加速版｜图生视频高效出片方案_2105118748511399938.json, 视频生成/文生视频/加速版MiniMax H3图生视频首尾帧视频工作流，文生视频视频运镜图生视频_2107890229058297858.json, 视频生成/文生视频/加速版首尾帧视频生成｜MiniMax H3图生视频运镜控制_2097043511534243841.json, 视频生成/文生视频/首尾帧精准控制 MiniMax H3图生视频加速版流畅出片_2104266521487958017.json, 视频生成/文生视频/首尾帧视频加速版｜MiniMax H3图生视频生成_2094749515961163777.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/首尾帧图文一键生视频｜MiniMax H3加速版数字人_2095958370124656641.json、视频生成/图生视频/首尾帧生视频！加速版MiniMaxH3转场特效数字人图生视频_2085455030794145794.json、视频生成/文生视频/5秒1080p仅8分钟｜MiniMax-H3图生视频全节点注释版_2093768843360563202.json、视频生成/文生视频/5秒1080p只要8分钟｜MiniMax-H3图生视频全节点注释_2094005447392063489.json、视频生成/文生视频/5秒1080p文生视频8分钟出片 MiniMax-H3 全节点注释_2094187651468455937.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 18 个 workflow 都包含：
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
- `MiniMaxH3ImageToVideo`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 17/18 个有
- `Int` —— 16/18 个有
- `CR Prompt Text` —— 14/18 个有
- `ImageResizeKJv2` —— 14/18 个有
- `ShowAnything|Mie` —— 14/18 个有
- `CM_IntToFloat` —— 13/18 个有
- `SaveImage` —— 8/18 个有
- `ResolutionSelector` —— 5/18 个有
- `CR Text` —— 3/18 个有
- `GetNode` —— 2/18 个有
- `PrimitiveFloat` —— 2/18 个有
- `SetNode` —— 2/18 个有
- `AILab_QwenVL_Advanced` —— 1/18 个有
- `DF_Int_to_Float` —— 1/18 个有
- `Image Stitch` —— 1/18 个有
- `ImageScaleDownToSize` —— 1/18 个有
- `LayerUtility: PurgeVRAM` —— 1/18 个有
- `easy imageScaleDownToSize` —— 1/18 个有
- `easy positive` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
