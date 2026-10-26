---
name: unknown_workflow_sampler_unet_vae_192
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.869833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/miniMax H3图生视频_2084688950412795906.json, 视频生成/图生视频/minimax_h3_i2v  加速多参考视频生成_2106315178865422338.json, 视频生成/图生视频/minimax_h3_i2v  加速首位帧_2106309679268843522.json, 视频生成/图生视频/minimax_h3_图生视频_2084112158757052417.json, 视频生成/图生视频/调用版minimax+H3+开源版 -首尾帧_2091060784687308801.json, 视频生成/图生视频/调用版minimax+H3+开源版+文生视频+T2VA文生_2086814099383607297.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_192

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/miniMax H3图生视频_2084688950412795906.json、视频生成/图生视频/minimax_h3_i2v  加速多参考视频生成_2106315178865422338.json、视频生成/图生视频/minimax_h3_i2v  加速首位帧_2106309679268843522.json、视频生成/图生视频/minimax_h3_图生视频_2084112158757052417.json、视频生成/图生视频/调用版minimax+H3+开源版 -首尾帧_2091060784687308801.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `H3SigmaRefiner` —— 2/6 个有
- `LoraLoaderBypassModelOnly` —— 2/6 个有
- `ModelAttentionBackend` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `DuckHideNode` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `SeedVR2LoadDiTModel` —— 1/6 个有
- `SeedVR2LoadVAEModel` —— 1/6 个有
- `SeedVR2VideoUpscaler` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
