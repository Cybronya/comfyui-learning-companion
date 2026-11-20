---
name: unknown_workflow_video_sampler_vae_70
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.843125
common_nodes: [ImagePadKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX+2倍加速Phantom电商视频编辑V1_1936769465738514434.json, 视频生成/图生视频/Phantom 14B人物一致性编辑V1加速版（支持电商）_1927406902211416066.json, 视频生成/图生视频/Phantom14b多图参考_1927371436502192130.json, 视频生成/图生视频/Skyreel V3 多参考图 图生视频_2017619701119066113.json, 视频生成/图生视频/SkyreelV3参考图生视频_2016868591383093249.json, 视频生成/图生视频/SkyreelV3参考图生视频（效果很一般，但是人物一致性保持的挺好 可以玩玩） 林耀_2017268862005284866.json, 视频生成/图生视频/SkyreelV3参考图生视频（极速版）_2017057905576513537.json, 视频生成/图生视频/SkyreelV3多图参考生视频_2017128536502439937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_70

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/FusionX+2倍加速Phantom电商视频编辑V1_1936769465738514434.json、视频生成/图生视频/Phantom 14B人物一致性编辑V1加速版（支持电商）_1927406902211416066.json、视频生成/图生视频/Phantom14b多图参考_1927371436502192130.json、视频生成/图生视频/Skyreel V3 多参考图 图生视频_2017619701119066113.json、视频生成/图生视频/SkyreelV3参考图生视频_2016868591383093249.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `ImagePadKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 7/8 个有
- `ImageResizeKJ` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `INTConstant` —— 6/8 个有
- `easy imageRemBg` —— 6/8 个有
- `FlashVSRNode` —— 5/8 个有
- `CR Prompt Text` —— 3/8 个有
- `WanVideoTeaCache` —— 3/8 个有
- `GetNode` —— 2/8 个有
- `JWInteger` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `ImageConcanate` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PDIMAGE_LongerSize` —— 1/8 个有
- `Text` —— 1/8 个有
- `VHS_Unbatch` —— 1/8 个有
- `WanVideoVRAMManagement` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
