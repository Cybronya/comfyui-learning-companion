---
name: unknown_workflow_sampler_unet_vae_166
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.7845
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/最强开源视频！Minimax-h3 图生电商视频_2084291715531362305.json, 数字人/数字人/benson  声音克隆数字人_2097164489119588353.json, 视频生成/图生视频/H3-图生视频-首尾帧_2087831020287643649.json, 视频生成/图生视频/MiniMax+H3图生视频（首帧视频、尾帧视频、首尾帧视频）_2084465463463075842.json, 视频生成/图生视频/minimax_h3_迷你别墅视频工作流_2084267933227900930.json, 视频生成/图生视频/minimax_h3图生视频（稳定）_2085014325353340930.json, 视频生成/图生视频/video_minimax_h3_i2v_2084124570839240705.json, 视频生成/文生视频/Minimax H3 全系列工作流【AI小王子】_2084162640192032770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_166

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/最强开源视频！Minimax-h3 图生电商视频_2084291715531362305.json、数字人/数字人/benson  声音克隆数字人_2097164489119588353.json、视频生成/图生视频/H3-图生视频-首尾帧_2087831020287643649.json、视频生成/图生视频/MiniMax+H3图生视频（首帧视频、尾帧视频、首尾帧视频）_2084465463463075842.json、视频生成/图生视频/minimax_h3_迷你别墅视频工作流_2084267933227900930.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 7/8 个有
- `MiniMaxH3ImageToVideo` —— 7/8 个有
- `GetImageSize` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `MiniMaxH3ReferenceToVideo` —— 2/8 个有
- `AudioCrop` —— 1/8 个有
- `Dapao_LlamaCaption` —— 1/8 个有
- `Dapao_LlamaCaptionOptions` —— 1/8 个有
- `ImageCrop+` —— 1/8 个有
- `ImpactConditionalBranch` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RegexReplace` —— 1/8 个有
- `easy boolean` —— 1/8 个有
- `easy showAnything` —— 1/8 个有
- `ttN int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
