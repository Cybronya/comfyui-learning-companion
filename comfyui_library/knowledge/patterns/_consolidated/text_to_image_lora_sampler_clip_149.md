---
name: text_to_image_lora_sampler_clip_149
type: Text To Image
frequency: 11
level: strong
coverage: 0.792818
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimax h3 i2v fastH3 contextmotion longvideo 图生视频_2105127145923244034.json, 视频生成/图生视频/minimax h3 i2v fastH3 图生视频快速生成方案_2108665137354862594.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_v2_veda，图生视频极速版_2111247286016761857.json, 视频生成/图生视频/minimax_h3_rawmodel_veta注意力参考，图生视频方案_2111248740865634306.json, 视频生成/图生视频/minimax_h3_rawmodel参考生视频精品，数字人动作迁移_2111244078024323074.json, 视频生成/图生视频/minimax_h3多图快速参考生视频，文生图图生视频_2111236219102384130.json, 视频生成/图生视频/三图参考无参考音｜Minimax H3图生视频人物一致性生成_2089442281551130625.json, 视频生成/图生视频/双图参考无音频｜Minimax H3图生视频一致性生成_2089443599820873730.json, 视频生成/图生视频/开源版minimax h3 i2v fastH3快速图生视频精品 高质量动态生成_2108709377132818433.json, 视频生成/图生视频/自行车图生视频测试工作流，图生视频处理方案_2106875364315324417.json, 视频生成/图生视频/自行车图生视频测试工作流，图生视频处理方案_2109447261494272002.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_149

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/minimax h3 i2v fastH3 contextmotion longvideo 图生视频_2105127145923244034.json、视频生成/图生视频/minimax h3 i2v fastH3 图生视频快速生成方案_2108665137354862594.json、视频生成/图生视频/minimax_h3_i2v_fastH3_v2_veda，图生视频极速版_2111247286016761857.json、视频生成/图生视频/minimax_h3_rawmodel_veta注意力参考，图生视频方案_2111248740865634306.json、视频生成/图生视频/minimax_h3_rawmodel参考生视频精品，数字人动作迁移_2111244078024323074.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 11 个 workflow 都包含：
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
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 10/11 个有
- `BlockSparseAttention` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `SaveImage` —— 9/11 个有
- `VHS_VideoCombine` —— 9/11 个有
- `MiniMaxH3ReferenceToVideo` —— 7/11 个有
- `SetNode` —— 7/11 个有
- `GetNode` —— 6/11 个有
- `MiniMaxH3SigmaShift` —— 6/11 个有
- `ModelAttentionBackend` —— 6/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/11 个有
- `MiniMaxH3ImageToVideo` —— 4/11 个有
- `VedaSparseAttention` —— 4/11 个有
- `MiniMaxH3MotionContext` —— 3/11 个有
- `MiniMaxH3MotionContextChain` —— 3/11 个有
- `MiniMaxH3MotionContextLoadLatent` —— 3/11 个有
- `MiniMaxH3MotionContextSaveLatent` —— 3/11 个有
- `MiniMaxH3MotionContextTrim` —— 3/11 个有
- `QwenH3PromptLocal` —— 3/11 个有
- `CreateVideo` —— 2/11 个有
- `GetVideoComponents` —— 2/11 个有
- `INTConstant` —— 2/11 个有
- `LoadAudio` —— 2/11 个有
- `LoadVideo` —— 2/11 个有
- `SaveVideo` —— 2/11 个有
- `Text Multiline` —— 2/11 个有
- `ViggleAnimateConditioningWindowed` —— 2/11 个有
- `EmptyImage` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `PreviewImage` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
