---
name: unknown_workflow_video_sampler_vae_47
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.892222
common_nodes: [ImageConcatMulti, ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/B4-Wan2.1多图融合视频phantom FusionX+NAG_1934069009803300865.json, 视频生成/图生视频/Phantom 14B人物一致性编辑V1加速版（支持电商）_1927406902211416066.json, 视频生成/图生视频/Phantom14b多图参考_1927371436502192130.json, 视频生成/图生视频/Skyreel V3 多参考图 图生视频_2017619701119066113.json, 视频生成/图生视频/SkyreelV3参考图生视频_2016868591383093249.json, 视频生成/图生视频/SkyreelV3参考图生视频（效果很一般，但是人物一致性保持的挺好 可以玩玩） 林耀_2017268862005284866.json, 视频生成/图生视频/SkyreelV3参考图生视频（极速版）_2017057905576513537.json, 视频生成/图生视频/SkyreelV3多图参考生视频_2017128536502439937.json, 视频生成/图生视频/phantom FusionX+NAG_1933786059002007553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_47

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/B4-Wan2.1多图融合视频phantom FusionX+NAG_1934069009803300865.json、视频生成/图生视频/Phantom 14B人物一致性编辑V1加速版（支持电商）_1927406902211416066.json、视频生成/图生视频/Phantom14b多图参考_1927371436502192130.json、视频生成/图生视频/Skyreel V3 多参考图 图生视频_2017619701119066113.json、视频生成/图生视频/SkyreelV3参考图生视频_2016868591383093249.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `easy imageRemBg` —— 8/9 个有
- `WanVideoTextEncode` —— 7/9 个有
- `FlashVSRNode` —— 5/9 个有
- `WanVideoTeaCache` —— 4/9 个有
- `CR Prompt Text` —— 2/9 个有
- `WanVideoApplyNAG` —— 2/9 个有
- `WanVideoTextEncodeSingle` —— 2/9 个有
- `GetNode` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `JWInteger` —— 1/9 个有
- `PDIMAGE_LongerSize` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `Text` —— 1/9 个有
- `WanVideoVRAMManagement` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
