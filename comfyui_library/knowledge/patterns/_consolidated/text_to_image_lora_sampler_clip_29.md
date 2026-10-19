---
name: text_to_image_lora_sampler_clip_29
type: Text To Image
frequency: 17
level: strong
coverage: 0.881353
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3图片换头 图生视频人物替换处理生成工具_2100269102773395458.json, 视频生成/图生视频/H3图片换头生视频 图生视频创作处理工具_2100267469515608066.json, 视频生成/图生视频/MiniMax H3参考生视频加速版｜加速LoRA图生视频生成_2097403914214789122.json, 视频生成/图生视频/MiniMax H3图片参考生成带货视频 加速版电商内容制作_2098699036625821698.json, 视频生成/图生视频/MiniMax H3开源加速版，音频驱动图片跳舞人物特效_2110843023394435074.json, 视频生成/图生视频/MiniMax H3开源加速版｜音频驱动图片跳舞人物特效出片_2110731793975570434.json, 视频生成/图生视频/MiniMax H3开源图片跳舞加速｜音频驱动角色设计图生视频_2110734968224837633.json, 视频生成/图生视频/MiniMax H3开源音频驱动图片跳舞｜加速版人物特效_2094874446220840962.json, 视频生成/图生视频/MiniMax H3开源音频驱动图片跳舞｜加速版角色表演_2094881447520858113.json, 视频生成/图生视频/图片跳舞｜MiniMax H3开源加速版，音频驱动角色表演_2099882356789301249.json, 视频生成/图生视频/数字人音频驱动图片跳舞加速版 MiniMax H3开源人物类特效方案_2093215341110452226.json, 视频生成/图生视频/数字人音频驱动图片跳舞加速｜MiniMax H3开源人物特效图生视频_2089726628791406594.json, 视频生成/图生视频/数字人音频驱动图片跳舞｜MiniMax H3开源人物类特效加速版_2091293535025844225.json, 视频生成/图生视频/音频驱动&图片跳舞｜MiniMax H3开源加速版生成_2095081150728462338.json, 视频生成/图生视频/音频驱动图片跳舞加速版开源｜MiniMax H3人物类特效角色设计图生视频_2088105811947114497.json, 视频生成/图生视频/音频驱动图片跳舞数字人｜MiniMax H3开源人物特效加速版_2093758821327007745.json, 视频生成/图生视频/音频驱动图片跳舞｜MiniMax H3开源加速，人物类特效一步到位_2099894171938152449.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/H3图片换头 图生视频人物替换处理生成工具_2100269102773395458.json、视频生成/图生视频/H3图片换头生视频 图生视频创作处理工具_2100267469515608066.json、视频生成/图生视频/MiniMax H3参考生视频加速版｜加速LoRA图生视频生成_2097403914214789122.json、视频生成/图生视频/MiniMax H3图片参考生成带货视频 加速版电商内容制作_2098699036625821698.json、视频生成/图生视频/MiniMax H3开源加速版，音频驱动图片跳舞人物特效_2110843023394435074.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 16/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 16/17 个有
- `SaveVideo` —— 16/17 个有
- `PrimitiveFloat` —— 15/17 个有
- `ResolutionSelector` —— 15/17 个有
- `LoadAudio` —— 14/17 个有
- `PathchSageAttentionKJ` —— 14/17 个有
- `PrimitiveStringMultiline` —— 14/17 个有
- `GetNode` —— 13/17 个有
- `LayerUtility: PurgeVRAM V2` —— 13/17 个有
- `PainterVRAM` —— 13/17 个有
- `SetNode` —— 13/17 个有
- `VRAM_Debug` —— 13/17 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 13/17 个有
- `SaveImage` —— 5/17 个有
- `CR Color Panel` —— 2/17 个有
- `GetImageSize` —— 2/17 个有
- `ImageCompositeMasked` —— 2/17 个有
- `Int` —— 2/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/17 个有
- `PreviewAny` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `RH_LLMAPI_Pro_Node` —— 2/17 个有
- `Text Multiline` —— 2/17 个有
- `Seed (rgthree)` —— 1/17 个有
- `easy saveVideo` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（19/17 个样本）：Steps较低可能导致细节不足
