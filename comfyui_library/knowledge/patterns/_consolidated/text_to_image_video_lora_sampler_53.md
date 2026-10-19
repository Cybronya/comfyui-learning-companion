---
name: text_to_image_video_lora_sampler_53
type: Text To Image
frequency: 13
level: strong
coverage: 0.754385
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3自定义sigma参数工作流，文生视频视频生视频全能_2110448826346729474.json, 视频生成/图生视频/Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482.json, 视频生成/图生视频/TaoMate MiniMax H3加速3步采样视频生成处理工具_2101045862658043905.json, 视频生成/图生视频/api竖屏540p坤坤H3官流｜图生视频轻量出片工作流_2108371168330866690.json, 视频生成/图生视频/api竖屏768p坤坤H3官流｜高清图生视频出片工作流_2108380600238428161.json, 视频生成/图生视频/lightx2v 8step加速｜MiniMax H3图生视频快速出片_2088748531585736705.json, 视频生成/图生视频/minimax h3 i2v fastH3 图生视频快速生成方案_2108665137354862594.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_v2_veda，图生视频极速版_2111247286016761857.json, 视频生成/图生视频/minimax_h3_rawmodel_veta注意力参考，图生视频方案_2111248740865634306.json, 视频生成/图生视频/minimax_h3_rawmodel参考生视频精品，数字人动作迁移_2111244078024323074.json, 视频生成/图生视频/minimax_h3多图快速参考生视频，文生图图生视频_2111236219102384130.json, 视频生成/图生视频/全能参考数字人｜AITUDOU MiniMax H3 人物音频一致性_2089296635812737025.json, 视频生成/图生视频/开源版minimax h3 i2v fastH3快速图生视频精品 高质量动态生成_2108709377132818433.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_53

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3自定义sigma参数工作流，文生视频视频生视频全能_2110448826346729474.json、视频生成/图生视频/Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482.json、视频生成/图生视频/TaoMate MiniMax H3加速3步采样视频生成处理工具_2101045862658043905.json、视频生成/图生视频/api竖屏540p坤坤H3官流｜图生视频轻量出片工作流_2108371168330866690.json、视频生成/图生视频/api竖屏768p坤坤H3官流｜高清图生视频出片工作流_2108380600238428161.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 12/13 个有
- `LoadImage` —— 12/13 个有
- `BlockSparseAttention` —— 10/13 个有
- `PrimitiveFloat` —— 10/13 个有
- `PrimitiveStringMultiline` —— 10/13 个有
- `MiniMaxH3ReferenceToVideo` —— 9/13 个有
- `SaveImage` —— 9/13 个有
- `SetNode` —— 9/13 个有
- `GetNode` —— 8/13 个有
- `ModelAttentionBackend` —— 7/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/13 个有
- `LoadAudio` —— 4/13 个有
- `VedaSparseAttention` —— 4/13 个有
- `ManualSigmas` —— 3/13 个有
- `MiniMaxH3ImageToVideo` —— 3/13 个有
- `MiniMaxH3SigmaShift` —— 3/13 个有
- `ModelPreviewOverrideKJ` —— 3/13 个有
- `QwenH3PromptLocal` —— 3/13 个有
- `Float` —— 2/13 个有
- `MiniMaxChunkFeedForward` —— 2/13 个有
- `MiniMaxLowVRAMAttention` —— 2/13 个有
- `PreviewAny` —— 2/13 个有
- `SigmasGraph` —— 2/13 个有
- `Text` —— 2/13 个有
- `CR Text` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `MiniMaxH3Unified` —— 1/13 个有
- `RH_LLMAPI_Pro_Node` —— 1/13 个有
- `ZNGB_AudioCrop` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
