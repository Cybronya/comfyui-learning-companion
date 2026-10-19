---
name: text_to_image_lora_sampler_clip_49
type: Text To Image
frequency: 15
level: strong
coverage: 0.841867
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3开源 动作迁移一键复刻｜MiniMaxH3图生视频舞蹈复制动作复刻_2092940607059746817.json, 视频生成/图生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086421628958892033.json, 视频生成/图生视频/H3开源全能参考生视频MiniMax视频生视频图生视频_2086445639256330242.json, 视频生成/图生视频/H3开源加速版海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版MiniMax_2099068104457416705.json, 视频生成/图生视频/H3开源加速版海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版MiniMax_2099074502104805378.json, 视频生成/图生视频/H3开源加速版海螺多参流｜漫剧短剧多宫格稳定出片，MiniMax速度加持_2099533253412745217.json, 视频生成/图生视频/H3视频换背景编辑 人物类特效处理生成工具_2100299115996467202.json, 视频生成/图生视频/MiniMax H3动作迁移方案｜视频动作迁移一键生成｜图生视频跟拍神器_2102273180428759042.json, 视频生成/图生视频/MiniMax H3动作迁移解决方案一键生成图生视频处理工具_2102511481890889729.json, 视频生成/图生视频/MiniMax H3视频换背景编辑支持参考图视频处理工具_2101414264681615362.json, 视频生成/图生视频/MiniMax-H3视频编辑神器｜一键视频换背景人物类特效_2107652623632519170.json, 视频生成/图生视频/MiniMaxH3动作模仿迁移｜高质量视频生成_2095592289065332737.json, 视频生成/图生视频/MiniMaxH3动作迁移 人物角色替换_2105103613914865665.json, 视频生成/图生视频/MiniMaxH3动作迁移神器｜一键套用动作出片超简单_2111088198364516353.json, 视频生成/图生视频/MiniMaxH3动作迁移｜角色动作复刻视频生成利器_2106614000522973186.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_49

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/H3开源 动作迁移一键复刻｜MiniMaxH3图生视频舞蹈复制动作复刻_2092940607059746817.json、视频生成/图生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086421628958892033.json、视频生成/图生视频/H3开源全能参考生视频MiniMax视频生视频图生视频_2086445639256330242.json、视频生成/图生视频/H3开源加速版海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版MiniMax_2099068104457416705.json、视频生成/图生视频/H3开源加速版海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版MiniMax_2099074502104805378.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 14/15 个有
- `PrimitiveStringMultiline` —— 14/15 个有
- `LoadImage` —— 13/15 个有
- `VAEDecodeAudio` —— 13/15 个有
- `VHS_VideoCombine` —— 13/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/15 个有
- `VHS_LoadVideo` —— 10/15 个有
- `孤海注释` —— 9/15 个有
- `ResolutionSelector` —— 8/15 个有
- `AILab_QwenVL` —— 7/15 个有
- `DF_Int_to_Float` —— 7/15 个有
- `ImageConcanate` —— 7/15 个有
- `ImageResizeKJv2` —— 7/15 个有
- `JoinStrings` —— 7/15 个有
- `PrimitiveInt` —— 7/15 个有
- `CreateVideo` —— 5/15 个有
- `EasyCache` —— 5/15 个有
- `SaveVideo` —— 5/15 个有
- `Fast Groups Bypasser (rgthree)` —— 4/15 个有
- `GetNode` —— 4/15 个有
- `SetNode` —— 4/15 个有
- `easy imageRemBg` —— 4/15 个有
- `LayerUtility: PurgeVRAM V2` —— 3/15 个有
- `ModelPatchTorchSettings` —— 3/15 个有
- `SaveImage` —— 3/15 个有
- `VRAM_Debug` —— 3/15 个有
- `FlashVSRNode` —— 2/15 个有
- `Int` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `CR Prompt Text` —— 1/15 个有
- `EmptyImage` —— 1/15 个有
- `PreviewImage` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（21/15 个样本）：Steps较低可能导致细节不足
