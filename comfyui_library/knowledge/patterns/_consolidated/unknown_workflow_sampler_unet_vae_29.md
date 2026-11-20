---
name: unknown_workflow_sampler_unet_vae_29
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.8183
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Pika版 MinimaxH3 图生视频！1080P+高帧率+15秒=10分钟！B站艾橘溪_2116794592455647233.json, 视频生成/图生视频/Pika版 MinimaxH3 图生视频！1080P+高帧率+15秒=10分钟！_2116833004709564417.json, 视频生成/图生视频/Pika版 MinimaxH3 图生视频！1080P+高帧率+15秒=10分钟！_2116881988404731905.json, 视频生成/图生视频/Pika版_MinimaxH3_图生视频！1080P+高帧率+15秒=10分钟！B站_2117027368366858242.json, 视频生成/图生视频/minimax-H3-flex-pika-单图参考_2116452087621046274.json, 视频生成/图生视频/minimax-H3-flex-pika-双图参考_2116452626291318785.json, 视频生成/图生视频/minimax_h3_i2v  加速多参考视频生成_2106315178865422338.json, 视频生成/图生视频/minimax_h3_i2v  加速首位帧_2106309679268843522.json, 视频生成/图生视频/minimax_h3_i2v_accel_2096897727664836609.json, 视频生成/图生视频/minimax_h3_i2v_videoonly_2090443654421897217.json, 视频生成/图生视频/minimax_h3_i2v图生视频_2084166438562127874.json, 视频生成/图生视频/minimax_h3_i2v官方首尾帧_2114194060029292545.json, 视频生成/图生视频/minimax_h3_图生视频_2084112158757052417.json, 视频生成/图生视频/minimax_h3_图生视频_2084537327996719106.json, 视频生成/图生视频/minimax_h3_图生视频_牛来_2094972668582916098.json, 视频生成/图生视频/minimax_h3_图生视频西瓜宝宝工作流_2084397677135089665.json, 视频生成/图生视频/minimax_h3_多图参考生视频_2097588393667551233.json, 视频生成/图生视频/video_minimax_h3_i2v 开源comfyui 官方版本_2084149773224992770.json, 视频生成/图生视频/图图 MiniMax H3 官方增强版图生视频工作流｜最高2K｜原生音轨_2085207381281169410.json, 视频生成/文生视频/图图 MiniMax H3 官方增强版文生视频工作流｜最高2K｜原生音轨_2085201060184018945.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_29

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/Pika版 MinimaxH3 图生视频！1080P+高帧率+15秒=10分钟！B站艾橘溪_2116794592455647233.json、视频生成/图生视频/Pika版 MinimaxH3 图生视频！1080P+高帧率+15秒=10分钟！_2116833004709564417.json、视频生成/图生视频/Pika版 MinimaxH3 图生视频！1080P+高帧率+15秒=10分钟！_2116881988404731905.json、视频生成/图生视频/Pika版_MinimaxH3_图生视频！1080P+高帧率+15秒=10分钟！B站_2117027368366858242.json、视频生成/图生视频/minimax-H3-flex-pika-单图参考_2116452087621046274.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 19/20 个有
- `LoadImage` —— 19/20 个有
- `VAEDecodeAudio` —— 19/20 个有
- `MiniMaxH3ImageToVideo` —— 17/20 个有
- `PrimitiveFloat` —— 16/20 个有
- `BasicScheduler` —— 14/20 个有
- `LoraLoaderModelOnly` —— 10/20 个有
- `GetImageSize` —— 8/20 个有
- `ImageScaleToTotalPixels` —— 8/20 个有
- `PrimitiveInt` —— 8/20 个有
- `PrimitiveStringMultiline` —— 8/20 个有
- `ComfySwitchNode` —— 6/20 个有
- `ManualSigmas` —— 6/20 个有
- `PrimitiveBoolean` —— 6/20 个有
- `JjkText` —— 5/20 个有
- `BlockSparseAttention` —— 4/20 个有
- `RTXVideoFrameGeneration` —— 4/20 个有
- `MiniMaxH3ReferenceToVideo` —— 3/20 个有
- `PreviewAny` —— 2/20 个有
- `StringConcatenate` —— 2/20 个有
- `TextGenerate` —— 2/20 个有
- `ImageScale` —— 1/20 个有
- `MiniMaxH3AddGuide` —— 1/20 个有
- `VideoCombineV2` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
