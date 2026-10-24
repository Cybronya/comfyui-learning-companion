---
name: unknown_workflow_video_lora_sampler_25
type: Unknown Workflow
frequency: 28
level: moderate
coverage: 0.611107
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/SteadDancer动作迁移_2017466618615439361.json, 视频生成/图生视频/SteadDancer动作迁移（支持动漫人物）长视频一致性加强版_2011405479620124674.json, 视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移_1995783729840787458.json, 视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移，超级Nice!好用到爆!_2039879176072732673.json, 视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移，超级Nice!好用到爆!_2046114909657763841.json, 视频生成/图生视频/SteadDancer视频姿势参考（KJ）_1996528847946399745.json, 视频生成/图生视频/SteadDancer视频自适应绑定动作迁移_1996396266479296514.json, 视频生成/图生视频/SteadyDancer  动作迁移 动作模仿  wan wan22 wan2.2_2077823494326415362.json, 视频生成/图生视频/SteadyDancer  动作迁移 动作模仿  wan wan22 wan2.2_2078124326972383233.json, 视频生成/图生视频/SteadyDancer  动作迁移 动作模仿  wan wan22 wan2.2_2087040327587815426.json, 视频生成/图生视频/SteadyDancer 动作迁移 动作模仿_2021045146128748546.json, 视频生成/图生视频/SteadyDancer 动作迁移 动作模仿_2021050493052657665.json, 视频生成/图生视频/SteadyDancer 动作迁移 动作模仿_2037367887756795905.json, 视频生成/图生视频/SteadyDancer 动作迁移_2012744356666544130.json, 视频生成/图生视频/SteadyDancer_动作迁移-顶级人类版_1999132133182631937.json, 视频生成/图生视频/SteadyDancer动作迁移_2037135094128844802.json, 视频生成/图生视频/SteadyDancer动作迁移_2037136001059000321.json, 视频生成/图生视频/SteadyDancer动作迁移_2037136442165563394.json, 视频生成/图生视频/SteadyDancer动作迁移_2043176583862689794.json, 视频生成/图生视频/SteadyDancer动作迁移_2073284965781032961.json, 视频生成/图生视频/SteadyDancer动作迁移_2074671640511868929.json, 视频生成/图生视频/SteadyDancer动作迁移_2080329957112377345.json, 视频生成/图生视频/SteadyDancer动作迁移_2080680922562781186.json, 视频生成/图生视频/SteadyDancer动作迁移_2084530681153146881.json, 视频生成/图生视频/口播 跳舞 带货皆可用 SteadyDancer动作迁移-_1999419556877791233.json, 视频生成/图生视频/视频二创-单人动作模仿_2019289437926068225.json, 视频生成/图生视频/跳舞_2020035033687396353.json, 视频生成/图生视频/（KJ版）SteadDancer视频姿势参考（新增骨骼绑定）_1995843794539098113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（视频生成/图生视频/SteadDancer动作迁移_2017466618615439361.json、视频生成/图生视频/SteadDancer动作迁移（支持动漫人物）长视频一致性加强版_2011405479620124674.json、视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移_1995783729840787458.json、视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移，超级Nice!好用到爆!_2039879176072732673.json、视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移，超级Nice!好用到爆!_2046114909657763841.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 28 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 27/28 个有
- `SetNode` —— 27/28 个有
- `WanVideoLoraSelect` —— 27/28 个有
- `WanVideoScheduler` —— 27/28 个有
- `GetImageSizeAndCount` —— 26/28 个有
- `WanVideoSetBlockSwap` —— 26/28 个有
- `ImageConcatMulti` —— 22/28 个有
- `PoseDetectionOneToAllAnimation` —— 22/28 个有
- `PreviewImage` —— 20/28 个有
- `WanVideoTorchCompileSettings` —— 20/28 个有
- `Int` —— 17/28 个有
- `CR Prompt Text` —— 16/28 个有
- `SimpleMath+` —— 15/28 个有
- `DrawViTPose` —— 12/28 个有
- `PoseAndFaceDetection` —— 12/28 个有
- `PrimitiveFloat` —— 10/28 个有
- `easy convertAnything` —— 9/28 个有
- `INTConstant` —— 4/28 个有
- `PrimitiveInt` —— 3/28 个有
- `CR Text` —— 2/28 个有
- `Fast Groups Muter (rgthree)` —— 2/28 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/28 个有
- `Anything Everywhere3` —— 1/28 个有
- `ImageConcanate` —— 1/28 个有
- `ImpactInt` —— 1/28 个有
- `Label (rgthree)` —— 1/28 个有
- `MathExpression|pysssss` —— 1/28 个有
- `ToFloat` —— 1/28 个有
- `WanVideoLoraSelectMulti` —— 1/28 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
