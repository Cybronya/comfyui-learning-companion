---
name: unknown_workflow_sampler_unet_vae_92
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.712667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/全能参考视频_Minimax H3_v2_2107298598168915969.json, 图片生成/图生图/剧情短片丨MiniMax H3丨双图参考·有声视频_2112107687327649793.json, 图片生成/图生图/海螺H3标准工作流-01-首尾帧生视频_2093944374529974273.json, 图片生成/图生图/海螺H3标准工作流-02-单图生视频_2093940538071412737.json, 图片生成/图生图/海螺H3标准工作流-03-人物参考跳舞_2093911326912503810.json, 平台全量/H3视频编辑-人物替换V2-优化加速_2105126476034170882.json, 平台全量/H3视频编辑-人物替换V2-优化加速_2105506228112814081.json, 平台全量/Minimax H3 视频编辑_2094315929038573570.json, 平台全量/电商产品替换_2112480922061856769.json, 平台全量/电商产品替换_2112481774365401089.json, 平台全量/短剧二创_2111169650137587714.json, 视频生成/文生视频/MinimaxH3+音频驱动多参_2092941359513694209.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_92

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/全能参考视频_Minimax H3_v2_2107298598168915969.json、图片生成/图生图/剧情短片丨MiniMax H3丨双图参考·有声视频_2112107687327649793.json、图片生成/图生图/海螺H3标准工作流-01-首尾帧生视频_2093944374529974273.json、图片生成/图生图/海螺H3标准工作流-02-单图生视频_2093940538071412737.json、图片生成/图生图/海螺H3标准工作流-03-人物参考跳舞_2093911326912503810.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `ModelAttentionBackend` —— 11/12 个有
- `SaveVideo` —— 11/12 个有
- `VAEDecodeAudio` —— 11/12 个有
- `ImageResizeKJv2` —— 10/12 个有
- `MiniMaxH3ReferenceToVideo` —— 10/12 个有
- `MiniMaxH3SigmaShift` —— 10/12 个有
- `easy int` —— 10/12 个有
- `PrimitiveInt` —— 9/12 个有
- `easy anythingIndexSwitch` —— 9/12 个有
- `GetImageSizeAndCount` —— 8/12 个有
- `VHS_LoadVideo` —— 8/12 个有
- `Bookmark (rgthree)` —— 7/12 个有
- `ComfyMathExpression` —— 7/12 个有
- `GetNode` —— 7/12 个有
- `PlaySound|pysssss` —— 7/12 个有
- `PrimitiveFloat` —— 7/12 个有
- `ResolutionSelector` —— 7/12 个有
- `SetNode` —— 7/12 个有
- `VHS_VideoCombine` —— 7/12 个有
- `VHS_VideoInfo` —— 7/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/12 个有
- `Label (rgthree)` —— 5/12 个有
- `LoadAudio` —— 2/12 个有
- `MiniMaxH3ImageToVideo` —— 2/12 个有
- `SaveImage` —— 2/12 个有
- `SoundFlow_GetLength` —— 2/12 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `INTConstant` —— 1/12 个有
- `ImageUpscaleWithModelBatched` —— 1/12 个有
- `Int` —— 1/12 个有
- `RIFE VFI` —— 1/12 个有
- `TrimAudioDuration` —— 1/12 个有
- `UpscaleModelLoader` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
