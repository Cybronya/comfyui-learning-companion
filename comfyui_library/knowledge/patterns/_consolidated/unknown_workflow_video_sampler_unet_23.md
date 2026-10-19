---
name: unknown_workflow_video_sampler_unet_23
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.875308
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2100863837363851266.json, 视频生成/图生视频/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2101132610901733377.json, 视频生成/图生视频/创意无限_2087087580423741441.json, 视频生成/图生视频/单图Minimax H3_2085688315197616129.json, 视频生成/图生视频/吉他和狗狗_2090264859219947522.json, 视频生成/图生视频/图生视频_2086720339278647297.json, 视频生成/图生视频/最新mimimaxH3漫剧镜头T1_2084662928074174466.json, 视频生成/图生视频/空白工作流MinimaxH3首尾帧创意视频T1_2086623709909053442.json, 视频生成/图生视频/首尾帧创意电商广告_2087187752570933249.json, 视频生成/图生视频/首尾帧欢乐小狗_2087363013287432194.json, 视频生成/图生视频/首尾帧生成广告视频_2087173880573157377.json, 视频生成/图生视频/首尾帧视频生成_2086728278747996161.json, 视频生成/文生视频/AITUDOU-MiniMax+H3+T2V（文生视频）加速流_2085602340672987137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_23

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2100863837363851266.json、视频生成/图生视频/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2101132610901733377.json、视频生成/图生视频/创意无限_2087087580423741441.json、视频生成/图生视频/单图Minimax H3_2085688315197616129.json、视频生成/图生视频/吉他和狗狗_2090264859219947522.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `MiniMaxH3ImageToVideo` —— 10/13 个有
- `ImageResizeKJv2` —— 9/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/13 个有
- `RHHiddenNodes` —— 9/13 个有
- `Text` —— 9/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/13 个有
- `ResolutionSelector` —— 4/13 个有
- `MiniMaxH3ReferenceToVideo` —— 3/13 个有
- `ImageScaleToTotalPixels` —— 2/13 个有
- `JjkText` —— 2/13 个有
- `LoraLoaderModelOnly` —— 2/13 个有
- `MiniMaxH3BlockCacheT8` —— 2/13 个有
- `GetNode` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `SetNode` —— 1/13 个有
- `easy showAnything` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
