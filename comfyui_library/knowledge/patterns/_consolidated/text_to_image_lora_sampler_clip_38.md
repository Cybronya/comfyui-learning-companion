---
name: text_to_image_lora_sampler_clip_38
type: Text To Image
frequency: 20
level: strong
coverage: 0.86985
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3加速版AI Video Studio PR插件｜VIP专用短剧生成优化版_2090085975216189442.json, 图片生成/图生图/MiniMax H3参考生视频量化加速版多模态处理工具_2101367524666470402.json, 图片生成/图生图/MiniMax H3视频换装带货展示，动作迁移服装呈现_2110826055559892993.json, 图片生成/图生图/MiniMax H3视频添加物品视频编辑，视频超分风格转换处理工具_2103899733600333826.json, 图片生成/图生图/MiniMaxH3视频添加物品编辑｜往已拍视频里塞新东西超简单_2103668392619237378.json, 图片生成/图生图/PR插件专用｜AI Video Studio短剧生成加速优化版直出_2089798943013167106.json, 数字人/数字人/人物场景替换工作流｜数字人一键换背景搬家不穿帮_2097578172031258626.json, 视频生成/图生视频/H3开源 动作迁移一键复刻｜MiniMaxH3图生视频舞蹈复制动作复刻_2092940607059746817.json, 视频生成/图生视频/H3视频换背景编辑 人物类特效处理生成工具_2100299115996467202.json, 视频生成/图生视频/MiniMax H3动作迁移方案｜视频动作迁移一键生成｜图生视频跟拍神器_2102273180428759042.json, 视频生成/图生视频/MiniMax H3动作迁移解决方案一键生成图生视频处理工具_2102511481890889729.json, 视频生成/图生视频/MiniMax H3开源加速版，音频驱动图片跳舞人物特效_2110843023394435074.json, 视频生成/图生视频/MiniMax H3开源加速版｜音频驱动图片跳舞人物特效出片_2110731793975570434.json, 视频生成/图生视频/MiniMax H3开源图片跳舞加速｜音频驱动角色设计图生视频_2110734968224837633.json, 视频生成/图生视频/MiniMax H3开源音频驱动图片跳舞｜加速版人物特效_2094874446220840962.json, 视频生成/图生视频/MiniMax H3开源音频驱动图片跳舞｜加速版角色表演_2094881447520858113.json, 视频生成/图生视频/MiniMax H3视频换背景编辑支持参考图视频处理工具_2101414264681615362.json, 视频生成/图生视频/MiniMaxH3动作模仿迁移｜高质量视频生成_2095592289065332737.json, 视频生成/图生视频/MiniMaxH3动作迁移 人物角色替换_2105103613914865665.json, 视频生成/图生视频/MiniMaxH3动作迁移神器｜一键套用动作出片超简单_2111088198364516353.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/MiniMax H3加速版AI Video Studio PR插件｜VIP专用短剧生成优化版_2090085975216189442.json、图片生成/图生图/MiniMax H3参考生视频量化加速版多模态处理工具_2101367524666470402.json、图片生成/图生图/MiniMax H3视频换装带货展示，动作迁移服装呈现_2110826055559892993.json、图片生成/图生图/MiniMax H3视频添加物品视频编辑，视频超分风格转换处理工具_2103899733600333826.json、图片生成/图生图/MiniMaxH3视频添加物品编辑｜往已拍视频里塞新东西超简单_2103668392619237378.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 20 个 workflow 都包含：
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
- `LoadImage` —— 19/20 个有
- `PathchSageAttentionKJ` —— 19/20 个有
- `孤海注释` —— 19/20 个有
- `PrimitiveStringMultiline` —— 18/20 个有
- `VAEDecodeAudio` —— 18/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 16/20 个有
- `ResolutionSelector` —— 13/20 个有
- `VHS_LoadVideo` —— 13/20 个有
- `VHS_VideoCombine` —— 12/20 个有
- `GetNode` —— 10/20 个有
- `LayerUtility: PurgeVRAM V2` —— 10/20 个有
- `SetNode` —— 10/20 个有
- `ImageConcanate` —— 9/20 个有
- `VRAM_Debug` —— 9/20 个有
- `CreateVideo` —— 8/20 个有
- `LoadAudio` —— 8/20 个有
- `SaveVideo` —— 8/20 个有
- `AILab_QwenVL` —— 7/20 个有
- `DF_Int_to_Float` —— 7/20 个有
- `ImageResizeKJv2` —— 7/20 个有
- `JoinStrings` —— 7/20 个有
- `PrimitiveInt` —— 7/20 个有
- `SaveImage` —— 7/20 个有
- `PainterVRAM` —— 5/20 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 5/20 个有
- `easy imageRemBg` —— 3/20 个有
- `CR Prompt Text` —— 2/20 个有
- `EasyCache` —— 2/20 个有
- `FlashVSRNode` —— 2/20 个有
- `ImageUpscaleWithModel` —— 2/20 个有
- `Int` —— 2/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/20 个有
- `UpscaleModelLoader` —— 2/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（22/20 个样本）：Steps较低可能导致细节不足
