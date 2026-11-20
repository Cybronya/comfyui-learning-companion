---
name: unknown_workflow_sampler_unet_vae_38
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.462944
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/开源版minimax_h3_i2v_fastH3音乐配乐生成_2117525280444211202.json, 视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json, 视频生成/图生视频/10eros_singularity_base james02_2115355058022993921.json, 视频生成/图生视频/10eros_singularity_base james02_2115944774216802306.json, 视频生成/图生视频/10eros_singularity_base_2115251799962767361.json, 视频生成/图生视频/10eros_singularity_base_2115301053825634305.json, 视频生成/图生视频/10eros_singularity_base_2115309980621557762.json, 视频生成/图生视频/AITUDOU-MiniMax H3(全能参考)_2084210400207396866.json, 视频生成/图生视频/AITUDOU-MiniMax H3(全能参考)真人短剧加速版_2084291490649567233.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+I2V+图生视频+1280分辨率加速流_2085330041017298945.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+I2V+（首帧）_2084283095339065346.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+T2V（文生视频）加速流_2085589980080070658.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+全能参考（1280分辨率）加速流_2085330061422579714.json, 视频生成/图生视频/AITUDOU-MiniMax-H3-FastVideo极速多参_2108436780260356097.json, 视频生成/图生视频/H3极速测试工作流_2109473161694760961.json, 视频生成/图生视频/MiniMax H3 DSW全能多参1280分辨率加速工作流_2092879864431988738.json, 视频生成/图生视频/MiniMax-H3-FastVideo多参极速版_2108479598177636354.json, 视频生成/图生视频/YZ金鱼-MiniMax H3超级多合一工作流-官方版_2093245007657521154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_38

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（平台全量/开源版minimax_h3_i2v_fastH3音乐配乐生成_2117525280444211202.json、视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json、视频生成/图生视频/10eros_singularity_base james02_2115355058022993921.json、视频生成/图生视频/10eros_singularity_base james02_2115944774216802306.json、视频生成/图生视频/10eros_singularity_base_2115251799962767361.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 17/18 个有
- `ResolutionSelector` —— 17/18 个有
- `VAEDecode` —— 17/18 个有
- `VHS_VideoCombine` —— 17/18 个有
- `GetNode` —— 16/18 个有
- `SetNode` —— 16/18 个有
- `PrimitiveFloat` —— 15/18 个有
- `MiniMaxH3ReferenceToVideo` —— 14/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 13/18 个有
- `ModelAttentionBackend` —— 11/18 个有
- `BlockSparseAttention` —— 10/18 个有
- `PrimitiveStringMultiline` —— 10/18 个有
- `Label (rgthree)` —— 9/18 个有
- `Text` —— 8/18 个有
- `ImageScaleToTotalPixels` —— 5/18 个有
- `LoraLoaderModelOnly` —— 5/18 个有
- `Fast Groups Bypasser (rgthree)` —— 4/18 个有
- `MiniMaxH3ImageToVideo` —— 4/18 个有
- `LoadAudio` —— 3/18 个有
- `easy float` —— 3/18 个有
- `MiniMaxH3SigmaShift` —— 2/18 个有
- `SigmasGraph` —— 2/18 个有
- `VHS_LoadVideo` —— 2/18 个有
- `EasyCache` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/18 个有
- `PreviewImage` —— 1/18 个有
- `QwenH3PromptLocal` —— 1/18 个有
- `SaveAudioAdvanced` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
