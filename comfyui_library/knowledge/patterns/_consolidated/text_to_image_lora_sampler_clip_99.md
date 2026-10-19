---
name: text_to_image_lora_sampler_clip_99
type: Text To Image
frequency: 9
level: strong
coverage: 0.752778
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3官方长视频续接｜图生视频无缝延长生成_2095203720807145474.json, 视频生成/图生视频/H3长视频音频驱动数字人唱歌30秒1分钟切换_2099933503063412738.json, 视频生成/图生视频/MiniMax H3参考生视频数字人 图生视频智能体创作_2098639055553646593.json, 视频生成/图生视频/MiniMax H3参考生视频｜数字人动作神态复刻_2098709684097212418.json, 视频生成/图生视频/MiniMax多参考生成视频R2V图生视频处理工具_2102478493312442370.json, 视频生成/图生视频/Minimax多帧插入视频续写，视频生视频拉长片段神器_2110489536747884545.json, 视频生成/图生视频/官方长视频续接无缝｜H3图生视频接续工作流_2095480320987582466.json, 视频生成/文生视频/minimax-H3 官方版去油提质｜长视频续接无限延长手动版_2096903551057481730.json, 视频生成/文生视频/去油提画质长视频续接｜MiniMax H3官方版无限延长手动生成_2096782492383666177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_99

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/H3官方长视频续接｜图生视频无缝延长生成_2095203720807145474.json、视频生成/图生视频/H3长视频音频驱动数字人唱歌30秒1分钟切换_2099933503063412738.json、视频生成/图生视频/MiniMax H3参考生视频数字人 图生视频智能体创作_2098639055553646593.json、视频生成/图生视频/MiniMax H3参考生视频｜数字人动作神态复刻_2098709684097212418.json、视频生成/图生视频/MiniMax多参考生成视频R2V图生视频处理工具_2102478493312442370.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 9 个 workflow 都包含：
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
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/9 个有
- `ComfySwitchNode` —— 6/9 个有
- `MiniMaxH3AddGuide` —— 6/9 个有
- `PrimitiveBoolean` —— 6/9 个有
- `TrimAudioDuration` —— 6/9 个有
- `VHS_LoadVideo` —— 6/9 个有
- `GetImageRangeFromBatch` —— 5/9 个有
- `GetNode` —— 5/9 个有
- `ImageAddNoise` —— 5/9 个有
- `SaveImage` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `ExtendIntermediateSigmas` —— 4/9 个有
- `ModelPreviewOverrideKJ` —— 4/9 个有
- `easy showAnything` —— 4/9 个有
- `MiniMaxH3SigmaShift` —— 3/9 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/9 个有
- `AudioConcat` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `PrimitiveInt` —— 2/9 个有
- `SolAttnPatch` —— 2/9 个有
- `AudioCrop` —— 1/9 个有
- `ColorMatchV2` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `Image Batch` —— 1/9 个有
- `ImageBatch` —— 1/9 个有
- `ImageFromBatch` —— 1/9 个有
- `ImageScale` —— 1/9 个有
- `SelectImages` —— 1/9 个有
- `easy minimaxH3AudioLock` —— 1/9 个有
- `忽略多组孤海` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
