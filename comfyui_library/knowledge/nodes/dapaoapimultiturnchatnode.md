# DapaoAPIMultiTurnChatNode

## 节点类型

`DapaoAPIMultiTurnChatNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `🤖API模型:DAPAO_API_LLM_CONFIG`（2 次）
- `⚙️对话设置:DAPAO_API_CHAT_SETTINGS`（2 次）
- `🧩Skill配置:DAPAO_API_SKILL_CONFIG`（2 次）
- `📦素材库:DAPAO_API_CHAT_MATERIAL_LIBRARY`（2 次）
- `💬本轮消息:STRING`（2 次）
- `📚会话历史:STRING`（2 次）
- `🖼️图片引用:STRING`（2 次）
- `🧩流程状态:STRING`（2 次）
- `🧩选项:STRING`（2 次）
- `🆔请求标识:STRING`（2 次）

## 输出

- `💬助手回复:STRING`（2 次）
- `📚会话历史JSON:STRING`（2 次）
- `🧩Skill最终结果:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "[]", "[]", "{}", "[]", "", "chat", ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
