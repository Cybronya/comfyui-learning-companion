---
name: text_to_image_lora_sampler_clip_46
type: Text To Image
frequency: 18
level: strong
coverage: 0.895333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3参考图像音频多模态输入｜视频生成工作流_2094512101560766466.json, 视频生成/图生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100640992356556801.json, 视频生成/图生视频/H3图生视频加速版｜快速高质量视频直出生成_2094902804635799554.json, 视频生成/图生视频/H3多图生视频_2085855343179026433.json, 视频生成/图生视频/H3多图生视频_2085861865661485058.json, 视频生成/图生视频/H3文生视频加速版｜快速直出高质量视频生成_2094509372390076418.json, 视频生成/图生视频/H3稳定加速版整合打斗和脸部修复Lora_2100265879845040129.json, 视频生成/图生视频/H3角色替换图生视频｜视频人物一键换脸替换生成_2088772291898466305.json, 视频生成/图生视频/H3角色替换图生视频｜视频人物一键换脸替换生成_2090466751896178689.json, 视频生成/图生视频/H3音频驱动数字人单人版｜口播视频高质量生成_2094900079206424577.json, 视频生成/图生视频/MINIMAX H3多模态生视频 参考图像视频音频全接口 视频生视频强机_2105036316378484738.json, 视频生成/图生视频/MINIMAX-H3多模态生视频｜参考图像视频音频全接口｜视频生视频强机_2104443942606561282.json, 视频生成/图生视频/MiniMax H3稳定加速版 整合脸部修复Lora高动态场景适配_2098641262172794881.json, 视频生成/图生视频/Minimax H3开源数字人，说话唱歌文生视频两不误_2111201846995017729.json, 视频生成/图生视频/Minimax H3开源版数字人说话唱歌 数字人口播方案_2109421181240700930.json, 视频生成/图生视频/单人版音频驱动数字人｜H3图生视频对口型生成_2095092471347900417.json, 视频生成/图生视频/开源稳定加速版全能参考｜MiniMax H3支持自定义音频图生视频_2091285576120102913.json, 音频生成/音频生成/声音克隆音频生成｜H3语音克隆工作流_2088159396017827842.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_46

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/H3参考图像音频多模态输入｜视频生成工作流_2094512101560766466.json、视频生成/图生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100640992356556801.json、视频生成/图生视频/H3图生视频加速版｜快速高质量视频直出生成_2094902804635799554.json、视频生成/图生视频/H3多图生视频_2085855343179026433.json、视频生成/图生视频/H3多图生视频_2085861865661485058.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
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
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 16/18 个有
- `LoadImage` —— 16/18 个有
- `ResolutionSelector` —— 16/18 个有
- `VHS_VideoCombine` —— 16/18 个有
- `SaveImage` —— 15/18 个有
- `孤海注释` —— 14/18 个有
- `LoraLoaderBypassModelOnly` —— 13/18 个有
- `MiniMaxH3ReferenceToVideo` —— 13/18 个有
- `VAEDecodeAudio` —— 12/18 个有
- `FlashVSRNode` —— 10/18 个有
- `PathchSageAttentionKJ` —— 10/18 个有
- `Sleep` —— 10/18 个有
- `VHS_LoadVideo` —— 8/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/18 个有
- `PainterVRAM` —— 6/18 个有
- `AudioCrop` —— 5/18 个有
- `PreviewAudio` —— 5/18 个有
- `CreateVideo` —— 4/18 个有
- `SaveVideo` —— 4/18 个有
- `SoundFlow_GetLength` —— 4/18 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/18 个有
- `EmptyImage` —— 3/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/18 个有
- `MiniMaxH3AudioConditioningT8` —— 3/18 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/18 个有
- `PreviewImage` —— 3/18 个有
- `Int` —— 2/18 个有
- `MiniMaxH3ImageToVideo` —— 2/18 个有
- `Audio Duration (mtb)` —— 1/18 个有
- `MathExpression|pysssss` —— 1/18 个有
- `ProcessString` —— 1/18 个有
- `SaveAudioAdvanced` —— 1/18 个有

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
| Steps较低可能导致细节不足 | 19/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（19/18 个样本）：Steps较低可能导致细节不足
