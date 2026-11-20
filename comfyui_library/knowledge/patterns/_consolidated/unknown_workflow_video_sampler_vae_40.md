---
name: unknown_workflow_video_sampler_vae_40
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8806
common_nodes: [INTConstant, ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Skyreels V3 多图参考生视频 sky r2v_2027315533716131841.json, 视频生成/图生视频/phantom多图参考一致性视频生成-电商带货_1917399608392089601.json, 视频生成/图生视频/phantom多图参考视频生成_1916457677722161154.json, 视频生成/图生视频/多参图片生视频skyreelsV3_2019240301956702210.json, 视频生成/图生视频/字节Phantom 14B_1927551955353374722.json, 视频生成/图生视频/最优参数Phantom14B多图参考_1927581509937422337.json, 视频生成/图生视频/最优参数Phantom14B多图参考_1971606625880567810.json, 视频生成/图生视频/龙明Phantom14b多图参考_1928697815218950145.json, 视频生成/图生视频/龙明phantom FusionX+NAG_1935045733223735298.json, 视频生成/图生视频/🔥Phantom初体验！AI带货视频制作指南 + ComfyUI保姆级教程_1930083460306649089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_40

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Skyreels V3 多图参考生视频 sky r2v_2027315533716131841.json、视频生成/图生视频/phantom多图参考一致性视频生成-电商带货_1917399608392089601.json、视频生成/图生视频/phantom多图参考视频生成_1916457677722161154.json、视频生成/图生视频/多参图片生视频skyreelsV3_2019240301956702210.json、视频生成/图生视频/字节Phantom 14B_1927551955353374722.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `INTConstant`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTextEncode` —— 9/10 个有
- `PreviewImage` —— 8/10 个有
- `WanVideoTeaCache` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `ImageConcatMulti` —— 7/10 个有
- `easy imageRemBg` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `Evaluate Integers` —— 1/10 个有
- `FlashVSRNode` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `Text _O` —— 1/10 个有
- `WanVideoApplyNAG` —— 1/10 个有
- `WanVideoTextEncodeSingle` —— 1/10 个有
- `WanVideoVRAMManagement` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
