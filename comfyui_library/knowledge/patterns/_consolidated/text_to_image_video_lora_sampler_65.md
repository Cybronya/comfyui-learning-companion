---
name: text_to_image_video_lora_sampler_65
type: Text To Image
frequency: 12
level: strong
coverage: 0.780167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3超写实数字人｜真假难分_2089545869266866177.json, 视频生成/图生视频/Minimax开源版H3多宫格图生视频开源版加速版_2086425565711654914.json, 视频生成/图生视频/TaoMate MiniMax H3加速3步采样视频生成处理工具_2101045862658043905.json, 视频生成/图生视频/api竖屏540p坤坤H3官流｜图生视频轻量出片工作流_2108371168330866690.json, 视频生成/图生视频/api竖屏768p坤坤H3官流｜高清图生视频出片工作流_2108380600238428161.json, 视频生成/图生视频/minimax h3 i2v fastH3 contextmotion longvideo 图生视频_2105127145923244034.json, 视频生成/图生视频/minimax h3 i2v fastH3 图生视频快速生成方案_2108665137354862594.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_v2_veda，图生视频极速版_2111247286016761857.json, 视频生成/图生视频/minimax_h3_rawmodel_veta注意力参考，图生视频方案_2111248740865634306.json, 视频生成/图生视频/minimax_h3_rawmodel参考生视频精品，数字人动作迁移_2111244078024323074.json, 视频生成/图生视频/minimax_h3多图快速参考生视频，文生图图生视频_2111236219102384130.json, 视频生成/图生视频/开源版minimax h3 i2v fastH3快速图生视频精品 高质量动态生成_2108709377132818433.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_65

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3超写实数字人｜真假难分_2089545869266866177.json、视频生成/图生视频/Minimax开源版H3多宫格图生视频开源版加速版_2086425565711654914.json、视频生成/图生视频/TaoMate MiniMax H3加速3步采样视频生成处理工具_2101045862658043905.json、视频生成/图生视频/api竖屏540p坤坤H3官流｜图生视频轻量出片工作流_2108371168330866690.json、视频生成/图生视频/api竖屏768p坤坤H3官流｜高清图生视频出片工作流_2108380600238428161.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 12 个 workflow 都包含：
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
- `VAEDecodeAudio` —— 11/12 个有
- `BlockSparseAttention` —— 10/12 个有
- `孤海注释` —— 10/12 个有
- `MiniMaxH3ReferenceToVideo` —— 8/12 个有
- `SaveImage` —— 8/12 个有
- `SetNode` —— 8/12 个有
- `GetNode` —— 7/12 个有
- `ModelAttentionBackend` —— 6/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/12 个有
- `LoadAudio` —— 4/12 个有
- `MiniMaxH3ImageToVideo` —— 4/12 个有
- `MiniMaxH3SigmaShift` —— 4/12 个有
- `VedaSparseAttention` —— 4/12 个有
- `QwenH3PromptLocal` —— 3/12 个有
- `ManualSigmas` —— 2/12 个有
- `ModelPreviewOverrideKJ` —— 2/12 个有
- `PathchSageAttentionKJ` —— 2/12 个有
- `MiniMaxH3MotionContext` —— 1/12 个有
- `MiniMaxH3MotionContextChain` —— 1/12 个有
- `MiniMaxH3MotionContextLoadLatent` —— 1/12 个有
- `MiniMaxH3MotionContextSaveLatent` —— 1/12 个有
- `MiniMaxH3MotionContextTrim` —— 1/12 个有
- `PainterVRAM` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `SaveAudio` —— 1/12 个有
- `TrimAudioDuration` —— 1/12 个有
- `VHS_LoadVideo` —— 1/12 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
