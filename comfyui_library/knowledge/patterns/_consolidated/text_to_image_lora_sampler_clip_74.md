---
name: text_to_image_lora_sampler_clip_74
type: Text To Image
frequency: 11
level: strong
coverage: 0.894
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax H3单人极速人物替换，角色一致性动作迁移_2110538185297186818.json, 视频生成/图生视频/Minimax H3参考生视频电商带货8步加速版工作流，服装展示图生视频方案_2108285549428699137.json, 视频生成/图生视频/Minimax H3双图参考双参考音｜图生视频多模态参考_2089737749720031234.json, 视频生成/图生视频/Minimax H3双图参考无参考音｜图生视频多图参考_2089736461087232001.json, 视频生成/图生视频/Minimax H3图生视频Lightx2v正式版生成工作流_2088211425947897858.json, 视频生成/图生视频/Minimax H3多参数Lightx2v加速图生视频生成_2088183351814479874.json, 视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2086034301048680450.json, 视频生成/图生视频/Minimax H3多图参考视频流｜全节点中文注释齐全，新手也能看懂_2099470227150032898.json, 视频生成/图生视频/Minimax H3多宫格加速版｜开源海螺多参出片｜漫剧短剧稳定量产_2102631344886075393.json, 视频生成/图生视频/Minimax H3电商带货参考生视频 8步加速版服装展示_2110352251444355074.json, 视频生成/图生视频/Minimax-H3多参长视频736p直出｜原版图生视频工作流_2097088563040051202.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Minimax H3单人极速人物替换，角色一致性动作迁移_2110538185297186818.json、视频生成/图生视频/Minimax H3参考生视频电商带货8步加速版工作流，服装展示图生视频方案_2108285549428699137.json、视频生成/图生视频/Minimax H3双图参考双参考音｜图生视频多模态参考_2089737749720031234.json、视频生成/图生视频/Minimax H3双图参考无参考音｜图生视频多图参考_2089736461087232001.json、视频生成/图生视频/Minimax H3图生视频Lightx2v正式版生成工作流_2088211425947897858.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 10/11 个有
- `PrimitiveFloat` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `CreateVideo` —— 7/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/11 个有
- `SaveVideo` —— 6/11 个有
- `VHS_VideoCombine` —— 6/11 个有
- `LoadAudio` —— 5/11 个有
- `PathchSageAttentionKJ` —— 5/11 个有
- `SaveImage` —— 4/11 个有
- `MiniMaxH3SigmaShift` —— 3/11 个有
- `EasyCache` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `INTConstant` —— 2/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `LoadVideoUI` —— 1/11 个有
- `MiniMaxH3MotionContext` —— 1/11 个有
- `MiniMaxH3MotionContextTrim` —— 1/11 个有
- `ModelAttentionBackend` —— 1/11 个有
- `ModelPatchTorchSettings` —— 1/11 个有
- `MuyeTextEditOutput` —— 1/11 个有
- `PainterVRAM` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `VHS_VideoInfoLoaded` —— 1/11 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/11 个有

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
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足
