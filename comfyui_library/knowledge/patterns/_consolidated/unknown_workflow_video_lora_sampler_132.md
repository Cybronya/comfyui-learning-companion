---
name: unknown_workflow_video_lora_sampler_132
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.674467
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Model Input Switch, ComfyMathExpression, GetImageSizeAndCount, GetNode, ImageResizeKJv2, KSamplerSelect, LTXVConcatAVLatent, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PreviewAny, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/MinimaxH3_导演台_r2v_满血_2115437832423694337.json, 图片生成/文生图/MinimaxH3_导演台_r2v_满血_2115662498983661569.json, 平台全量/MiniMax H3 导演台-视频生视频V2V_2092119064918454273.json, 平台全量/MinimaxH3 导演台 r2v_满血_2114458151763402753.json, 平台全量/MinimaxH3 导演台 r2v_满血new_2114575007484571649.json, 平台全量/MinimaxH3 导演台 rv2v_参考素材改视频_2号_2100238601266225153.json, 视频生成/图生视频/MiniMax H3 导演台-图生视频-手机端也能用_2091264120371892225.json, 视频生成/图生视频/MiniMax H3 导演台-手机端也可用_2090733228578656258.json, 视频生成/图生视频/MiniMax H3 导演台-首尾帧生视频-加速+二采+段间引导+手机端可用_2091271684509749249.json, 视频生成/文生视频/MiniMax H3 导演台-加速+二踩+段间引导-手机端也可用_2085217914751381506.json, 视频生成/文生视频/MiniMax H3 导演台-加速+二踩+段间引导-手机端也可用_2091070876266614786.json, 视频生成/文生视频/MiniMax H3 导演台-多参主图生视频_r2v_2091574959578632194.json, 视频生成/文生视频/MiniMax H3 导演台-多参主图生视频_r2v_2095126971830325249.json, 视频生成/文生视频/MinimaxH3 导演台 rv2v_参考素材改视频_优化版本_2092192766062321665.json, 视频生成/文生视频/阿清的minimaxh3导演台+2次采样工作流_2093210441047695362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_132

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/MinimaxH3_导演台_r2v_满血_2115437832423694337.json、图片生成/文生图/MinimaxH3_导演台_r2v_满血_2115662498983661569.json、平台全量/MiniMax H3 导演台-视频生视频V2V_2092119064918454273.json、平台全量/MinimaxH3 导演台 r2v_满血_2114458151763402753.json、平台全量/MinimaxH3 导演台 r2v_满血new_2114575007484571649.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Model Input Switch`
- `ComfyMathExpression`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 14/15 个有
- `LayerUtility: PurgeVRAM` —— 14/15 个有
- `LazySwitch1way` —— 14/15 个有
- `SaveVideo` —— 14/15 个有
- `easy boolean` —— 14/15 个有
- `MuyeLoadImage` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
