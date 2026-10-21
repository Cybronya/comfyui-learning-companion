---
name: unknown_workflow_sampler_vae_15
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.823765
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax H3 开源版图生视频_2084165222453039105.json, 视频生成/图生视频/minimax h3 竖屏版_2084459891346993153.json, 视频生成/图生视频/2078283699623391233.json, 视频生成/图生视频/minimax-h3首尾帧工作流_2086646638457737217.json, 视频生成/图生视频/minimaxH3 FL2VA 首尾帧_2093654739836825602.json, 视频生成/图生视频/minimax_h3_i2v_accel_2096897727664836609.json, 视频生成/图生视频/minimax_h3_i2v_videoonly_2090443654421897217.json, 视频生成/图生视频/minimax_h3_i2v图生视频_2084166438562127874.json, 视频生成/图生视频/minimax_h3_图生视频_2084537327996719106.json, 视频生成/图生视频/minimax_h3_图生视频_牛来_2094972668582916098.json, 视频生成/图生视频/minimax_h3_图生视频西瓜宝宝工作流_2084397677135089665.json, 视频生成/图生视频/minimax_h3_迷你别墅视频工作流_2084267933227900930.json, 视频生成/图生视频/video_minimax_h3_i2v_2084124570839240705.json, 视频生成/图生视频/video_minimax_h3_i2v_2087451619603603457.json, 视频生成/图生视频/【开源】minimax_h3 图生视频_2084171369004232706.json, 视频生成/图生视频/图图 MiniMax H3 官方增强版图生视频工作流｜最高2K｜原生音轨_2085207381281169410.json, 视频生成/文生视频/图图 MiniMax H3 官方增强版文生视频工作流｜最高2K｜原生音轨_2085201060184018945.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_15

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/minimax H3 开源版图生视频_2084165222453039105.json、视频生成/图生视频/minimax h3 竖屏版_2084459891346993153.json、视频生成/图生视频/2078283699623391233.json、视频生成/图生视频/minimax-h3首尾帧工作流_2086646638457737217.json、视频生成/图生视频/minimaxH3 FL2VA 首尾帧_2093654739836825602.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 16/17 个有
- `LoadImage` —— 15/17 个有
- `UNETLoader` —— 15/17 个有
- `GetImageSize` —— 11/17 个有
- `ImageScaleToTotalPixels` —— 11/17 个有
- `ComfySwitchNode` —— 4/17 个有
- `PrimitiveBoolean` —— 4/17 个有
- `Text` —— 3/17 个有
- `LoraLoaderModelOnly` —— 2/17 个有
- `PreviewAny` —— 2/17 个有
- `PrimitiveInt` —— 2/17 个有
- `PrimitiveStringMultiline` —— 2/17 个有
- `ResizeImageMaskNode` —— 2/17 个有
- `StringConcatenate` —— 2/17 个有
- `TextGenerate` —— 2/17 个有
- `UnetLoaderGGUF` —— 2/17 个有
- `ImageResizeKJv2` —— 1/17 个有
- `ImageScale` —— 1/17 个有
- `PreviewImage` —— 1/17 个有
- `TeaCache` —— 1/17 个有
- `YK_LoadImageFromURL` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
