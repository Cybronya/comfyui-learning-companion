---
name: unknown_workflow_sampler_vae_12
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.850524
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax H3 开源版图生视频_2084165222453039105.json, 视频生成/图生视频/minimax h3 竖屏版_2084459891346993153.json, 视频生成/图生视频/minimax-h3首尾帧工作流_2078283699623391233.json, 视频生成/图生视频/minimax-h3首尾帧工作流_2086646638457737217.json, 视频生成/图生视频/minimaxH3 FL2VA 首尾帧_2093654739836825602.json, 视频生成/图生视频/minimaxH3开源版尾帧生视频_2092343211615412226.json, 视频生成/图生视频/minimaxH3开源版首尾帧(20step)_2092293644232519681.json, 视频生成/图生视频/minimaxH3开源版首帧生视频_2092326575885869057.json, 视频生成/图生视频/minimax_h3_i2v_videoonly_2090443654421897217.json, 视频生成/图生视频/minimax_h3_i2v图生视频_2084166438562127874.json, 视频生成/图生视频/minimax_h3_图生视频_2084537327996719106.json, 视频生成/图生视频/minimax_h3_图生视频西瓜宝宝工作流_2084397677135089665.json, 视频生成/图生视频/minimax_h3_迷你别墅视频工作流_2084267933227900930.json, 视频生成/图生视频/video_minimax_h3_i2v 开源comfyui 官方版本_2084149773224992770.json, 视频生成/图生视频/video_minimax_h3_i2v_2084124570839240705.json, 视频生成/图生视频/video_minimax_h3_i2v_2087451619603603457.json, 视频生成/图生视频/【开源】minimax_h3 图生视频_2084171369004232706.json, 视频生成/图生视频/【老金驿站】MinimaxH3首尾帧视频工作流_2084263524121014274.json, 视频生成/图生视频/海螺图生视频_2085524828332843010.json, 视频生成/文生视频/MiniMax H3 加速版 图生视频 首尾帧生视频_2086653248143978497.json, 视频生成/文生视频/海螺H3首尾帧生视频_2087721274360553473.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_12

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/minimax H3 开源版图生视频_2084165222453039105.json、视频生成/图生视频/minimax h3 竖屏版_2084459891346993153.json、视频生成/图生视频/minimax-h3首尾帧工作流_2078283699623391233.json、视频生成/图生视频/minimax-h3首尾帧工作流_2086646638457737217.json、视频生成/图生视频/minimaxH3 FL2VA 首尾帧_2093654739836825602.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 21 个 workflow 都包含：
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
- `LoadImage` —— 20/21 个有
- `VAEDecodeAudio` —— 20/21 个有
- `UNETLoader` —— 19/21 个有
- `GetImageSize` —— 14/21 个有
- `ImageScaleToTotalPixels` —— 14/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/21 个有
- `Text` —— 3/21 个有
- `ImageResizeKJv2` —— 2/21 个有
- `ResizeImageMaskNode` —— 2/21 个有
- `UnetLoaderGGUF` —— 2/21 个有
- `BOOLConstant` —— 1/21 个有
- `EmptyImage` —— 1/21 个有
- `Fast Groups Bypasser (rgthree)` —— 1/21 个有
- `JjkText` —— 1/21 个有
- `LoraLoaderModelOnly` —— 1/21 个有
- `MiniMaxH3BlockCacheT8` —— 1/21 个有
- `PathchSageAttentionKJ` —— 1/21 个有
- `PreviewImage` —— 1/21 个有
- `TeaCache` —— 1/21 个有
- `YK_LoadImageFromURL` —— 1/21 个有
- `easy imageIndexSwitch` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
