---
name: unknown_workflow_sampler_unet_vae_61
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.803077
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/图图 MiniMax H3 官方增强版图生视频工作流｜最高2K｜原生音轨_2085207381281169410.json, 视频生成/图生视频/海螺Minimax H3_r2v 官方加速版_2091451868676452353.json, 视频生成/图生视频/（首尾帧 2图）MINIMAX H3  图生视频_2111267377957658625.json, 视频生成/文生视频/MiniMax_H3 多参考图生视频（可本地运行）_2084295736807739394.json, 视频生成/文生视频/Minimax H3 - 多参视频生成_2084608321469898754.json, 视频生成/文生视频/Minimax H3 - 多参视频生成_2092164049516711938.json, 视频生成/文生视频/Minimax H3 Veda 稀疏注意力8步极速版 文生视频_2108479691337326593.json, 视频生成/文生视频/azheng_2095047905232121858.json, 视频生成/文生视频/minimax_h3_文生_图生视频_2084261498850988033.json, 视频生成/文生视频/全模態影音生成，畫面與聲音一次算出來；支援首尾幀控制、內建 8 步 Turbo 開關_2100568061072994305.json, 视频生成/文生视频/图图 MiniMax H3 官方增强版文生视频工作流｜最高2K｜原生音轨_2085201060184018945.json, 视频生成/文生视频/海螺H3多宫格图生视频场景图生成短视频角色卡片图生成短视频_2086510723475263490.json, 视频生成/文生视频/海螺minimax_h3_多参_中文版，适配comfyui（自用）_2077373534669721601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_61

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/图图 MiniMax H3 官方增强版图生视频工作流｜最高2K｜原生音轨_2085207381281169410.json、视频生成/图生视频/海螺Minimax H3_r2v 官方加速版_2091451868676452353.json、视频生成/图生视频/（首尾帧 2图）MINIMAX H3  图生视频_2111267377957658625.json、视频生成/文生视频/MiniMax_H3 多参考图生视频（可本地运行）_2084295736807739394.json、视频生成/文生视频/Minimax H3 - 多参视频生成_2084608321469898754.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
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
- `LoadImage` —— 11/13 个有
- `PrimitiveStringMultiline` —— 11/13 个有
- `ComfySwitchNode` —— 7/13 个有
- `MiniMaxH3ReferenceToVideo` —— 7/13 个有
- `PrimitiveBoolean` —— 7/13 个有
- `MiniMaxH3ImageToVideo` —— 6/13 个有
- `LoraLoaderModelOnly` —— 5/13 个有
- `PrimitiveInt` —— 5/13 个有
- `GetImageSize` —— 3/13 个有
- `ImageScaleToTotalPixels` —— 3/13 个有
- `PreviewAny` —— 2/13 个有
- `StringConcatenate` —— 2/13 个有
- `TextGenerate` —— 2/13 个有
- `ImageScale` —— 1/13 个有
- `VedaSparseAttention` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
