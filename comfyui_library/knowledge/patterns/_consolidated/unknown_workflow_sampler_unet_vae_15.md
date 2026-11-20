---
name: unknown_workflow_sampler_unet_vae_15
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.81836
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/H3 首尾帧六步_2119876001248399361.json, 平台全量/H3+图生视频+1080P+高帧率+15秒+10分钟+H3++Image-to-Video_2120321909039656962.json, 平台全量/MiniMaxH3图生视频_2119694763724201985.json, 平台全量/MiniMaxH3文生视频 卡普冲击波_2120138844384358402.json, 平台全量/MiniMaxH3文生视频 大风车下女孩跑_2120123524114374657.json, 平台全量/MiniMaxH3文生视频 寸拳_2120126594214875137.json, 平台全量/MiniMaxH3文生视频 忍者房顶奔跑_2120105950400040962.json, 平台全量/MiniMaxH3文生视频_2119888868454522882.json, 平台全量/MinimaxH3 图生视频-Pika版_2117159668295495681.json, 平台全量/Pika H3 6步 文生视频_2117499603720433665.json, 平台全量/Pika H3 6步 首尾帧生视频_2117501577861885954.json, 平台全量/Pika H3 Flex：文生视频_2118860831298514945.json, 平台全量/Pika H3 Flex：首尾帧生视频_2118866868692930562.json, 平台全量/Pika版_MinimaxH3_图生视频！1080P+高帧率+15秒=10分钟！B站_2117469642993258498.json, 平台全量/pika_+minimaxh3速享首尾帧_2117473195891712002.json, 平台全量/你的AI桌面女友15秒只需8分钟极速版_2105721867242926082.json, 数字人/数字人/H3+图生视频 1080P+高帧率+15秒 10分钟 H3+ Image-to-Video_2117057758016139265.json, 视频生成/图生视频/2-MiniMax-H3-单图-首尾帧生视频工作流V2_2084639140699795458.json, 视频生成/图生视频/H3+pika 极速首尾帧视频_2116157600994783234.json, 视频生成/图生视频/Minimax H3 单张参考图生视频标准版_2102224374689517569.json, 视频生成/图生视频/Minimax H3 首尾帧图生视频标准版_2102237236300435457.json, 视频生成/图生视频/Minimax_H3_单张参考图生视频标准版_2102317605854990338.json, 视频生成/图生视频/Minimax_H3_首尾帧图生视频标准版_2104053564233568257.json, 视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2104052395767582721.json, 视频生成/图生视频/pika +minimaxh3速享首尾帧_2116473438524239874.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_15

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（平台全量/H3 首尾帧六步_2119876001248399361.json、平台全量/H3+图生视频+1080P+高帧率+15秒+10分钟+H3++Image-to-Video_2120321909039656962.json、平台全量/MiniMaxH3图生视频_2119694763724201985.json、平台全量/MiniMaxH3文生视频 卡普冲击波_2120138844384358402.json、平台全量/MiniMaxH3文生视频 大风车下女孩跑_2120123524114374657.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 25 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 24/25 个有
- `LoadImage` —— 18/25 个有
- `PrimitiveFloat` —— 18/25 个有
- `PrimitiveInt` —— 18/25 个有
- `ResolutionSelector` —— 17/25 个有
- `BasicScheduler` —— 13/25 个有
- `ManualSigmas` —— 12/25 个有
- `GetImageSize` —— 10/25 个有
- `ImageScaleToTotalPixels` —— 10/25 个有
- `BlockSparseAttention` —— 8/25 个有
- `ComfySwitchNode` —— 6/25 个有
- `PrimitiveBoolean` —— 6/25 个有
- `MiniMaxH3SigmaShift` —— 5/25 个有
- `ModelAttentionBackend` —— 5/25 个有
- `JjkText` —— 4/25 个有
- `RTXVideoFrameGeneration` —— 4/25 个有
- `EmptyImage` —— 3/25 个有
- `ModelPreviewOverrideKJ` —— 3/25 个有
- `PreviewImage` —— 3/25 个有
- `PrimitiveStringMultiline` —— 3/25 个有
- `Fast Groups Bypasser (rgthree)` —— 1/25 个有
- `MiniMaxH3ContextIR` —— 1/25 个有
- `ShowText|pysssss` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
