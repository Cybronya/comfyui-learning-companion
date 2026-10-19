---
name: text_to_image_video_lora_sampler_29
type: Text To Image
frequency: 17
level: strong
coverage: 0.883471
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3加速版文生视频｜文字一键快速生成视频工作流_2094732479742701569.json, 视频生成/图生视频/H3单图生视频｜MINIMAX工作流8-20新版_2090869883713179650.json, 视频生成/图生视频/H3参考图像音频多模态输入｜视频生成工作流_2094512101560766466.json, 视频生成/图生视频/H3图生视频加速版｜快速高质量视频直出生成_2094902804635799554.json, 视频生成/图生视频/H3多图生视频_2085855343179026433.json, 视频生成/图生视频/H3多图生视频_2085861865661485058.json, 视频生成/图生视频/H3文生视频加速版｜快速直出高质量视频生成_2094509372390076418.json, 视频生成/图生视频/H3角色替换图生视频｜视频人物一键换脸替换生成_2088772291898466305.json, 视频生成/图生视频/H3角色替换图生视频｜视频人物一键换脸替换生成_2090466751896178689.json, 视频生成/图生视频/H3音频驱动数字人单人版｜口播视频高质量生成_2094900079206424577.json, 视频生成/图生视频/MINIMAX H3多模态生视频 参考图像视频音频全接口 视频生视频强机_2105036316378484738.json, 视频生成/图生视频/MINIMAX-H3多模态生视频｜参考图像视频音频全接口｜视频生视频强机_2104443942606561282.json, 视频生成/图生视频/MinimaxH3多参音视频生成开源版（9图3视频3音频）ENGENG_2087124578177998850.json, 视频生成/图生视频/MinimaxH3开源版全能多参｜视频参考标准加速集合版_2095262567538192386.json, 视频生成/图生视频/单人版音频驱动数字人｜H3图生视频对口型生成_2095092471347900417.json, 视频生成/文生视频/MiNiMaxH3全能参考文生视频图生视频视频生视频普通加速版_2088368737501143041.json, 视频生成/文生视频/全能参考文生图生视频生视频｜MiNiMaxH3视频生成工作流_2088334930496548865.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_29

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/H3加速版文生视频｜文字一键快速生成视频工作流_2094732479742701569.json、视频生成/图生视频/H3单图生视频｜MINIMAX工作流8-20新版_2090869883713179650.json、视频生成/图生视频/H3参考图像音频多模态输入｜视频生成工作流_2094512101560766466.json、视频生成/图生视频/H3图生视频加速版｜快速高质量视频直出生成_2094902804635799554.json、视频生成/图生视频/H3多图生视频_2085855343179026433.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 16/17 个有
- `KSamplerSelect` —— 16/17 个有
- `LoadImage` —— 16/17 个有
- `LoraLoaderBypassModelOnly` —— 14/17 个有
- `LoadAudio` —— 13/17 个有
- `MiniMaxH3ReferenceToVideo` —— 13/17 个有
- `孤海注释` —— 13/17 个有
- `VAEDecodeAudio` —— 12/17 个有
- `VHS_LoadVideo` —— 11/17 个有
- `FlashVSRNode` —— 10/17 个有
- `SaveImage` —— 10/17 个有
- `Sleep` —— 10/17 个有
- `PathchSageAttentionKJ` —— 8/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/17 个有
- `PainterVRAM` —— 6/17 个有
- `AudioCrop` —— 5/17 个有
- `MiniMaxH3AVDecodeT8` —— 4/17 个有
- `MiniMaxH3AudioConditioningT8` —— 4/17 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 4/17 个有
- `CreateVideo` —— 3/17 个有
- `MiniMaxH3ImageToVideo` —— 3/17 个有
- `SaveVideo` —— 3/17 个有
- `忽略多组孤海` —— 3/17 个有
- `EmptyImage` —— 2/17 个有
- `PreviewAudio` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `SoundFlow_GetLength` —— 2/17 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/17 个有
- `RH_LLMAPI_Pro_Node` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（18/17 个样本）：Steps较低可能导致细节不足
