---
name: unknown_workflow_video_sampler_vae_20
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.950357
common_nodes: [ImagePadKJ, ImageResizeKJ, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Skyreelsv3-人物与物品一致视频生成_2020431913210617857.json, 视频生成/图生视频/Skyreelsv3-人物与物品一致视频生成tvc广告短视频_2029224724693262338.json, 视频生成/图生视频/skyreelsv3+主体一致性 (1)_2019437337008148481.json, 视频生成/图生视频/万相Phantom14B图片编辑工作流_1927590039822438402.json, 视频生成/图生视频/多图参考视频媲美可灵1.6_1925799442136666113.json, 视频生成/图生视频/字节Phantom14B_最新多图参考一致性视频_1927541511028903938.json, 视频生成/图生视频/字节Phantom14B图生视频_1927944176032464897.json, 视频生成/图生视频/字节Phantom14B最新主体一致性(电商广告视频生成)_1915051981709242369.json, 视频生成/图生视频/数字人电商带货FusionX-Phantom加速版14B_2039636071985713154.json, 视频生成/图生视频/数字人电商带货FusionX-Phantom加速版14B_2064931253647929346.json, 视频生成/图生视频/电商带货FusionX-Phantom加速版14B_1934089550950260738.json, 视频生成/图生视频/电商带货FusionX-Phantom加速版14B_2108761890527735810.json, 视频生成/图生视频/电商带货服装包包直播视频生成FusionX-Phantom加速版_1934241189509951489.json, 视频生成/文生视频/电商带货替换_1935520036046176257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_20

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/Skyreelsv3-人物与物品一致视频生成_2020431913210617857.json、视频生成/图生视频/Skyreelsv3-人物与物品一致视频生成tvc广告短视频_2029224724693262338.json、视频生成/图生视频/skyreelsv3+主体一致性 (1)_2019437337008148481.json、视频生成/图生视频/万相Phantom14B图片编辑工作流_1927590039822438402.json、视频生成/图生视频/多图参考视频媲美可灵1.6_1925799442136666113.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 14 个 workflow 都包含：
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 12/14 个有
- `WanVideoTextEncode` —— 12/14 个有
- `WanVideoTorchCompileSettings` —— 11/14 个有
- `Primitive integer [Crystools]` —— 10/14 个有
- `Text Multiline` —— 8/14 个有
- `ImageConcatMulti` —— 7/14 个有
- `PreviewImage` —— 7/14 个有
- `WanVideoTeaCache` —— 5/14 个有
- `easy clearCacheAll` —— 5/14 个有
- `INTConstant` —— 4/14 个有
- `CR Prompt Text` —— 2/14 个有
- `SimpleMath+` —— 2/14 个有
- `WanVideoTextEncodeCached` —— 2/14 个有
- `ImageResizeKJv2` —— 1/14 个有
- `SetNode` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
