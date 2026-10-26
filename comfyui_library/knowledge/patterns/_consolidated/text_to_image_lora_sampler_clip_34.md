---
name: text_to_image_lora_sampler_clip_34
type: Text To Image
frequency: 21
level: strong
coverage: 0.811333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多模态参考数字人对口型图生视频处理工具_2101006638630129665.json, 视频生成/图生视频/MiniMax H3开源加速版，音频驱动图片跳舞人物特效_2110843023394435074.json, 视频生成/图生视频/MiniMax H3开源加速版｜音频驱动图片跳舞人物特效出片_2110731793975570434.json, 视频生成/图生视频/MiniMax H3开源图片跳舞加速｜音频驱动角色设计图生视频_2110734968224837633.json, 视频生成/图生视频/MiniMax H3开源音频驱动图片跳舞｜加速版人物特效_2094874446220840962.json, 视频生成/图生视频/MiniMax H3开源音频驱动图片跳舞｜加速版角色表演_2094881447520858113.json, 视频生成/图生视频/MiniMax H3视频换背景编辑支持参考图视频处理工具_2101414264681615362.json, 视频生成/图生视频/MiniMax h3开源加速版 海螺多参文生视频图生视频音频参考_2085303974785273857.json, 视频生成/图生视频/MiniMax-H3视频编辑神器｜一键视频换背景人物类特效_2107652623632519170.json, 视频生成/图生视频/MiniMaxH3视频换背景编辑，视频生视频人物特效处理_2113101437289984001.json, 视频生成/图生视频/MiniMaxH3视频换背景编辑｜人物特效+运镜图生视频处理_2108372748677500929.json, 视频生成/图生视频/MiniMaxH3视频换背景，人物类特效视频生视频编辑器_2111274575668531202.json, 视频生成/图生视频/MiniMaxH3视频换背景｜视频编辑动作迁移生成_2095972447886598146.json, 视频生成/图生视频/MiniMaxH3视频背景替换编辑，其它视频处理全能手_2111278750330605570.json, 视频生成/图生视频/MiniMax_H3动作迁移图生视频_自定义背景人物全能参考_2101088561767473154.json, 视频生成/图生视频/MiniMax_H3视频换背景视频编辑工作流，人物类特效视频生视频处理工具_2109456422231699458.json, 视频生成/图生视频/MiniMax_H3视频换背景视频编辑工作流，人物类特效视频生视频处理方案_2109457359675412482.json, 视频生成/图生视频/图片跳舞｜MiniMax H3开源加速版，音频驱动角色表演_2099882356789301249.json, 视频生成/图生视频/心然寻源MiniMax H3多模态参考数字人对口型｜图生视频_2100764134798352386.json, 视频生成/图生视频/改版1｜数字人视频生成利器，老牌工作流焕新升级再战_2107327256866676738.json, 视频生成/图生视频/改版1｜数字人视频生成利器，老牌工作流焕新升级再战_2107440188136972289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多模态参考数字人对口型图生视频处理工具_2101006638630129665.json、视频生成/图生视频/MiniMax H3开源加速版，音频驱动图片跳舞人物特效_2110843023394435074.json、视频生成/图生视频/MiniMax H3开源加速版｜音频驱动图片跳舞人物特效出片_2110731793975570434.json、视频生成/图生视频/MiniMax H3开源图片跳舞加速｜音频驱动角色设计图生视频_2110734968224837633.json、视频生成/图生视频/MiniMax H3开源音频驱动图片跳舞｜加速版人物特效_2094874446220840962.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 19/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 18/21 个有
- `PrimitiveStringMultiline` —— 18/21 个有
- `PathchSageAttentionKJ` —— 16/21 个有
- `LayerUtility: PurgeVRAM V2` —— 15/21 个有
- `VRAM_Debug` —— 15/21 个有
- `孤海注释` —— 14/21 个有
- `LoadImage` —— 13/21 个有
- `LoadAudio` —— 12/21 个有
- `VHS_LoadVideo` —— 11/21 个有
- `VHS_VideoCombine` —— 11/21 个有
- `CreateVideo` —— 10/21 个有
- `SaveVideo` —— 10/21 个有
- `ImageConcanate` —— 9/21 个有
- `PreviewImage` —— 9/21 个有
- `EmptyImage` —— 8/21 个有
- `SaveImage` —— 8/21 个有
- `PainterVRAM` —— 6/21 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 6/21 个有
- `CR Prompt Text` —— 3/21 个有
- `Float` —— 2/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/21 个有
- `MiniMaxH3SLAPrecisionV2T8Advanced` —— 2/21 个有
- `MiniMaxH3SigmaShift` —— 2/21 个有
- `PreviewAudio` —— 2/21 个有
- `SigmasGraph` —— 2/21 个有
- `ZNGB_AudioCrop` —— 2/21 个有
- `Fast Groups Bypasser (rgthree)` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 21 | 100% |
| 采样算法 | er_sde | - | 21 | 100% |
| 调度器 | beta | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| 宽度 | 80 | 80 - 80 | 21 | 100% |
| 高度 | 80 | 80 - 80 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高发问题（21/21 个样本）：Steps较低可能导致细节不足
