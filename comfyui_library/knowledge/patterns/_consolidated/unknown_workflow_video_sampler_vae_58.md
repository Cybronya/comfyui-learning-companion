---
name: unknown_workflow_video_sampler_vae_58
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.869
common_nodes: [INTConstant, ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Skyreels V3 多图参考生视频 sky r2v_2027315533716131841.json, 视频生成/图生视频/phantom FusionX+NAG_1933786059002007553.json, 视频生成/图生视频/phantom多图参考一致性视频生成-电商带货_1917399608392089601.json, 视频生成/图生视频/最优参数Phantom14B多图参考_1927581509937422337.json, 视频生成/图生视频/最优参数Phantom14B多图参考_1971606625880567810.json, 视频生成/图生视频/龙明Phantom14b多图参考_1928697815218950145.json, 视频生成/图生视频/龙明phantom FusionX+NAG_1935045733223735298.json, 视频生成/图生视频/🔥Phantom初体验！AI带货视频制作指南 + ComfyUI保姆级教程_1930083460306649089.json, 视频生成/文生视频/FusionX Phantom多图迁移视频工作流_1937481435781447681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_58

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Skyreels V3 多图参考生视频 sky r2v_2027315533716131841.json、视频生成/图生视频/phantom FusionX+NAG_1933786059002007553.json、视频生成/图生视频/phantom多图参考一致性视频生成-电商带货_1917399608392089601.json、视频生成/图生视频/最优参数Phantom14B多图参考_1927581509937422337.json、视频生成/图生视频/最优参数Phantom14B多图参考_1971606625880567810.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
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
- `PreviewImage` —— 8/9 个有
- `ImageConcatMulti` —— 7/9 个有
- `WanVideoTeaCache` —— 7/9 个有
- `WanVideoTextEncode` —— 7/9 个有
- `WanVideoTorchCompileSettings` —— 6/9 个有
- `easy imageRemBg` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `WanVideoApplyNAG` —— 2/9 个有
- `WanVideoTextEncodeSingle` —— 2/9 个有
- `Evaluate Integers` —— 1/9 个有
- `FlashVSRNode` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `Text _O` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
