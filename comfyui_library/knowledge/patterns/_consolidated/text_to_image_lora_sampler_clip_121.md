---
name: text_to_image_lora_sampler_clip_121
type: Text To Image
frequency: 13
level: strong
coverage: 0.885
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/加速版图生视频｜H3高质量快速生成工作流_2095093795384811522.json, 视频生成/图生视频/加速版图生视频｜MiniMaxH3人物特效快速出片_2093142943912783874.json, 视频生成/图生视频/加速版图生视频｜h3图片转视频工作流_2088324394362957826.json, 视频生成/图生视频/动作迁移图生视频｜Minimax视频动作迁移工作流_2087218060968161281.json, 视频生成/图生视频/单人数字人直播｜MiniMax H3图生视频驱动口播_2089027921309691906.json, 视频生成/图生视频/单人版数字人直播｜MiniMax H3图生视频口播生成_2088700833398607873.json, 视频生成/图生视频/单人版音频驱动数字人｜H3图生视频对口型生成_2095092471347900417.json, 视频生成/图生视频/参考生视频Sage加速｜MiniMax H3数字人视频处理2608_2095551559856902146.json, 视频生成/图生视频/图像+视频+音频参考｜H3生成视频多模态工作流_2094735141095694338.json, 视频生成/图生视频/对口型音频驱动MiniMax H3数字人唱歌工作流，一张图一段音频生成视频_2106864466716614658.json, 视频生成/图生视频/海螺H3全能参考生视频加速开源版 9图3视频3音频多模态输入_2105370711207538690.json, 视频生成/文生视频/9图3视频3音频全能多参音视频生成开源加速版｜海螺H3文生图生视频工作流_2088148034331963394.json, 视频生成/文生视频/H3阿里3步加速Lora全能参考速度起飞_2100295935514468353.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_121

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/加速版图生视频｜H3高质量快速生成工作流_2095093795384811522.json、视频生成/图生视频/加速版图生视频｜MiniMaxH3人物特效快速出片_2093142943912783874.json、视频生成/图生视频/加速版图生视频｜h3图片转视频工作流_2088324394362957826.json、视频生成/图生视频/动作迁移图生视频｜Minimax视频动作迁移工作流_2087218060968161281.json、视频生成/图生视频/单人数字人直播｜MiniMax H3图生视频驱动口播_2089027921309691906.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
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
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 11/13 个有
- `PathchSageAttentionKJ` —— 11/13 个有
- `PrimitiveStringMultiline` —— 11/13 个有
- `LoadAudio` —— 9/13 个有
- `VAEDecodeAudio` —— 9/13 个有
- `VHS_VideoCombine` —— 9/13 个有
- `SaveImage` —— 7/13 个有
- `CreateVideo` —— 6/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/13 个有
- `VHS_LoadVideo` —— 6/13 个有
- `SaveVideo` —— 5/13 个有
- `AudioCrop` —— 4/13 个有
- `EasyCache` —— 4/13 个有
- `FlashVSRNode` —— 4/13 个有
- `LoraLoaderBypassModelOnly` —— 4/13 个有
- `Sleep` —— 4/13 个有
- `SoundFlow_GetLength` —— 4/13 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/13 个有
- `SolAttnPatch` —— 3/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `MiniMaxH3ImageToVideo` —— 2/13 个有
- `PainterVRAM` —— 2/13 个有
- `PreviewAudio` —— 2/13 个有
- `CR Prompt Text` —— 1/13 个有
- `FlashVSRInitPipe` —— 1/13 个有
- `FlashVSRNodeAdv` —— 1/13 个有
- `RTXVideoSuperResolution` —— 1/13 个有
- `SpectrumApplyMiniMaxH3` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
