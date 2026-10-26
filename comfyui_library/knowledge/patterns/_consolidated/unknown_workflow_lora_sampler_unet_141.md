---
name: unknown_workflow_lora_sampler_unet_141
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.4994
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, GetNode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, QwenEditConfigPreparer, ReferenceLatent, SaveImage, SetNode, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, easy convertAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QT110-人物多角度（全身）多视角 多视图 人物换角度 AI漫剧 人物一致性_2047933016995008514.json, 图片生成/图生图/QT110-人物多角度（半身）多视角 多视图 人物换角度 AI漫剧 人物一致性_2048217963689418753.json, 图片生成/图生图/QT110-人物多角度（大半身）多视角 多视图 人物换角度 AI漫剧 人物一致性_2047956369776582657.json, 图片生成/图生图/QT110-人物多角度（面部）多视角 多视图 人物换角度 AI漫剧 人物一致性_2048282953586843650.json, 图片生成/图生图/QT110-多角度编辑（Qwen-Edit）多视角 多视图 人物换角度 场景编辑 镜头编辑 AI漫剧_2046170535477911554.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_141

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/QT110-人物多角度（全身）多视角 多视图 人物换角度 AI漫剧 人物一致性_2047933016995008514.json、图片生成/图生图/QT110-人物多角度（半身）多视角 多视图 人物换角度 AI漫剧 人物一致性_2048217963689418753.json、图片生成/图生图/QT110-人物多角度（大半身）多视角 多视图 人物换角度 AI漫剧 人物一致性_2047956369776582657.json、图片生成/图生图/QT110-人物多角度（面部）多视角 多视图 人物换角度 AI漫剧 人物一致性_2048282953586843650.json、图片生成/图生图/QT110-多角度编辑（Qwen-Edit）多视角 多视图 人物换角度 场景编辑 镜头编辑 AI漫剧_2046170535477911554.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy convertAnything`

**可变部分**（部分 workflow 才有）：
- `IfInnerExecute` —— 4/5 个有
- `ImageFlip+` —— 4/5 个有
- `Int` —— 4/5 个有
- `IntConditions` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `RHHiddenNodes` —— 4/5 个有
- `LayerUtility: CropByMask` —— 3/5 个有
- `LayerUtility: ImageRemoveAlpha` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `Mute / Bypass Relay (rgthree)` —— 1/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `QwenMultiangleCameraNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 5 | 100% |
| 高度 | 1920 | 1920 - 1920 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 93/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，5 个样本，取值集中（一致性 100%）
- 高发问题（93/5 个样本）：Steps较低可能导致细节不足
