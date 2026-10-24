---
name: unknown_workflow_sampler_unet_vae_87
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.779909
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3融合底模 参考图一键生成环绕运镜视频（刻晴演示）_2103328135499567105.json, 视频生成/图生视频/MiniMax H3音画同步参考工作流_2091481322647805954.json, 视频生成/图生视频/MiniMax H3：参考生视频_2095783894242127874.json, 视频生成/图生视频/MiniMax H3：参考生视频（加速）_2096113080844513282.json, 视频生成/图生视频/MiniMax H3｜武打导演工作流 9组预设_2109867240077217794.json, 视频生成/图生视频/MiniMax_H3_七套服装连续换装_2094786595428847617.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2102924951413153793.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2103672100170067969.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2104844242353999874.json, 视频生成/图生视频/Minimax H3 Veda 稀疏注意力8步极速版 首尾帧_2108488300557328386.json, 视频生成/图生视频/R2V-参考生视频-5060Ti16G-极速加速版_2102730812373422081.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_87

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3融合底模 参考图一键生成环绕运镜视频（刻晴演示）_2103328135499567105.json、视频生成/图生视频/MiniMax H3音画同步参考工作流_2091481322647805954.json、视频生成/图生视频/MiniMax H3：参考生视频_2095783894242127874.json、视频生成/图生视频/MiniMax H3：参考生视频（加速）_2096113080844513282.json、视频生成/图生视频/MiniMax H3｜武打导演工作流 9组预设_2109867240077217794.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `ComfySwitchNode` —— 9/11 个有
- `LoraLoaderModelOnly` —— 9/11 个有
- `PrimitiveBoolean` —— 9/11 个有
- `PrimitiveInt` —— 9/11 个有
- `LoadAudio` —— 7/11 个有
- `MiniMaxH3SigmaShift` —— 3/11 个有
- `MiniMaxH3ImageToVideo` —— 2/11 个有
- `ModelAttentionBackend` —— 2/11 个有
- `BlockSparseAttention` —— 1/11 个有
- `H3SLAAttention` —— 1/11 个有
- `MiniMaxH3MotionContextSaveLatent` —— 1/11 个有
- `MiniMaxH3QwenReferencePrefixCacheT8Advanced` —— 1/11 个有
- `MinimaxH3LatentUpscaler3DRefineHandoff` —— 1/11 个有
- `ModelPatchTorchSettings` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `SpectrumSDXLBatch` —— 1/11 个有
- `VedaSparseAttention` —— 1/11 个有
- `XB_ReferenceAny` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
