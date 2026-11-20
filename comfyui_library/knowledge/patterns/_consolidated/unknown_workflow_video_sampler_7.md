---
name: unknown_workflow_video_sampler_7
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.821765
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/全能视频S一键去水印（短视频）_1983901528870322178.json, 平台全量/全能视频S去水印丨竖屏丨一键去水印_1983446444357165058.json, 平台全量/全能视频S去水印竖屏_1976523537932525570.json, 平台全量/全能视频S去水印竖版视频_精准水印遮罩_1973574883416346625.json, 平台全量/全能视频S横屏视频动态去水印消除（保留音频）_1973565788865081346.json, 平台全量/全能视频S横版16：9视频动态水印消除T8+SeddVR2二次视频高清_1974749437245435905.json, 平台全量/全能视频S横版视频动态水印消除V6（支持音频）_1973413814060322817.json, 平台全量/全能视频S竖屏视频动态去水印消除（保留音频）_1973557467013623810.json, 平台全量/全能视频S竖版9_16视频动态水印消除T8+SeddVR2二次视频高清_1974742651343908865.json, 平台全量/全能视频S竖版9_16视频动态水印消除T8+SeddVR2二次视频高清v6_1974842419839676418.json, 平台全量/全能视频S竖版视频动态水印消除V6（支持音频）_1973405691832610818.json, 平台全量/全能视频S竖版视频动态水印消除V6（支持音频）浮云 1.4_2007638340367028225.json, 平台全量/全能视频S竖版视频动态水印消除_1974097596102873089.json, 平台全量/横版16_9去水印-去动态水印 视频去水印-豆包seedance2.0动态水印_2025194015934648321.json, 平台全量/竖版9_16去水印-去动态水印 视频去水印-豆包seedance2.0动态水印_2025154855626612738.json, 平台全量/视频去水印，全能视频S去水印_1976623914866577409.json, 平台全量/视频去水印，全能视频s去水印，适合旧版的全能视频S_1973611158601076737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_7

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（平台全量/全能视频S一键去水印（短视频）_1983901528870322178.json、平台全量/全能视频S去水印丨竖屏丨一键去水印_1983446444357165058.json、平台全量/全能视频S去水印竖屏_1976523537932525570.json、平台全量/全能视频S去水印竖版视频_精准水印遮罩_1973574883416346625.json、平台全量/全能视频S横屏视频动态去水印消除（保留音频）_1973565788865081346.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 17 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 14/17 个有
- `ImageConcanate` —— 13/17 个有
- `MaskToImage` —— 13/17 个有
- `easy showAnything` —— 13/17 个有
- `PreviewImage` —— 11/17 个有
- `ImageFromBatch+` —— 7/17 个有
- `easy cleanGpuUsed` —— 6/17 个有
- `SaveImage` —— 5/17 个有
- `SeedVR2` —— 3/17 个有
- `Bookmark (rgthree)` —— 2/17 个有
- `CM_IntToBool` —— 2/17 个有
- `JWStringToInteger` —— 2/17 个有
- `RH_LLMAPI_NODE` —— 2/17 个有
- `easy ifElse` —— 2/17 个有
- `GetImageSize` —— 1/17 个有
- `ImageScale` —— 1/17 个有
- `ImageToMask` —— 1/17 个有
- `easy compare` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
